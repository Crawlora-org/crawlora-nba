package net.crawlora.nba;

import com.sun.net.httpserver.HttpServer;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.net.InetSocketAddress;
import java.time.Duration;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicReference;

import static org.junit.jupiter.api.Assertions.*;

class ClientTest {
    private HttpServer server;
    private volatile int status = 200;
    private volatile String contentType = "application/json";
    private volatile String body = "{\"ok\":true}";
    private volatile long delayMillis;
    private final AtomicReference<String> seenKey = new AtomicReference<>();
    private final AtomicReference<String> seenUri = new AtomicReference<>();
    private String baseUrl;

    @BeforeEach void startServer() throws Exception {
        server = HttpServer.create(new InetSocketAddress("127.0.0.1", 0), 0);
        server.createContext("/", exchange -> {
            seenKey.set(exchange.getRequestHeaders().getFirst("x-api-key"));
            seenUri.set(exchange.getRequestURI().toASCIIString());
            try { if (delayMillis > 0) Thread.sleep(delayMillis); }
            catch (InterruptedException error) { Thread.currentThread().interrupt(); }
            byte[] bytes = body.getBytes(java.nio.charset.StandardCharsets.UTF_8);
            exchange.getResponseHeaders().set("Content-Type", contentType);
            exchange.sendResponseHeaders(status, bytes.length);
            try (var output = exchange.getResponseBody()) { output.write(bytes); }
        });
        server.start();
        baseUrl = "http://127.0.0.1:" + server.getAddress().getPort() + "/api/v1";
    }

    @AfterEach void stopServer() { if (server != null) server.stop(0); }

    @Test void platformCatalogIsAnExactAllowlistAndExposesDirectMethod() throws Exception {
        assertEquals(70, Client.OPERATION_IDS.size());
        assertEquals(List.of("nba-box-score", "nba-box-score-advanced", "nba-box-score-defensive", "nba-box-score-four-factors", "nba-box-score-misc", "nba-box-score-player-track", "nba-box-score-scoring", "nba-box-score-summary", "nba-box-score-usage", "nba-common-all-players", "nba-draft-combine-anthro", "nba-enums", "nba-franchise-history", "nba-game-detail", "nba-games", "nba-homepage-leaders", "nba-homepage-v2", "nba-hustle-player", "nba-hustle-stats", "nba-hustle-team", "nba-league-game-log", "nba-lineup-shot-chart", "nba-lineups", "nba-news", "nba-opp-pt-shot", "nba-play-by-play", "nba-player-awards", "nba-player-bio-stats", "nba-player-career-stats", "nba-player-clutch", "nba-player-compare", "nba-player-dash-by-clutch", "nba-player-dash-by-game-splits", "nba-player-dash-by-last-n-games", "nba-player-dash-by-opponent", "nba-player-dash-pt-pass", "nba-player-dash-pt-reb", "nba-player-dash-pt-shots", "nba-player-game-logs", "nba-player-info", "nba-player-profile-v2", "nba-player-pt-shot", "nba-player-stats", "nba-player-streak-finder", "nba-players", "nba-playoff-picture", "nba-playoff-series", "nba-pt-defend", "nba-pt-stats", "nba-scoreboard", "nba-shot-chart", "nba-standings", "nba-synergy-play-types", "nba-team-dash-by-clutch", "nba-team-dash-by-game-splits", "nba-team-dash-by-last-n-games", "nba-team-dash-by-opponent", "nba-team-dash-pt-pass", "nba-team-dash-pt-reb", "nba-team-dash-pt-shots", "nba-team-details", "nba-team-game-logs", "nba-team-info-common", "nba-team-on-off", "nba-team-pt-shot", "nba-team-roster", "nba-team-shot-locations", "nba-team-stats", "nba-team-stats-leaders", "nba-team-years"), Client.OPERATION_IDS);
        assertEquals(new java.util.TreeSet<>(Client.OPERATION_IDS), new java.util.TreeSet<>(Client.operations().keySet()));
        assertEquals(Client.OPERATION_IDS.size(), new Client("key").getOperationCount());
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            assertThrows(IllegalArgumentException.class, () -> client.request("instagram-search", Map.of()));
            Object result = client.request("nba-box-score", Map.ofEntries(Map.entry("game_id", "value &/one")));
            assertInstanceOf(Map.class, result);
            assertEquals("test-key", seenKey.get());
            assertTrue(seenUri.get().startsWith("/api/v1/"));
            assertTrue(seenUri.get().contains("%26"), "query values should be URL encoded");
            // This operation has no path parameters to encode.
        }
    }

    @Test void directMethodUsesTheSameOperationDispatch() throws Exception {
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            Object result = Client.class.getMethod("boxScore", Map.class).invoke(client, Map.ofEntries(Map.entry("game_id", "value &/one")));
            assertInstanceOf(Map.class, result);
        }
    }

    @Test void returnsPlainTextWhenTheHostedResponseIsText() {
        contentType = "text/plain; charset=utf-8";
        body = "line one\nline two";
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            assertEquals("line one\nline two", client.request("nba-box-score", Map.ofEntries(Map.entry("game_id", "sample"))));
        }
    }

    @Test void surfacesHttpErrorsAndTimeouts() {
        status = 422;
        body = "{\"code\":422,\"msg\":\"bad input\"}";
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            CrawloraException error = assertThrows(CrawloraException.class,
                    () -> client.request("nba-box-score", Map.ofEntries(Map.entry("game_id", "value &/one"))));
            assertEquals(422, error.statusCode());
            assertTrue(error.getMessage().contains("bad input"));
        }
        status = 200;
        delayMillis = 250;
        try (Client client = new Client("test-key", baseUrl, Duration.ofMillis(20))) {
            assertThrows(CrawloraException.class, () -> client.request("nba-box-score", Map.ofEntries(Map.entry("game_id", "value &/one"))));
        }
    }

    @Test void rejectsInvalidEnumsAndClosedClientCalls() {
        assertThrows(IllegalArgumentException.class, () -> new Client("key", baseUrl, Duration.ofSeconds(1)).request("nba-box-score", Map.ofEntries(Map.entry("game_id", "sample"), Map.entry("league_id", "__invalid_java_test_enum__"))));
        Client client = new Client("key", baseUrl, Duration.ofSeconds(1));
        client.close();
        assertThrows(IllegalStateException.class, () -> client.request("nba-box-score", Map.ofEntries(Map.entry("game_id", "value &/one"))));
    }
}
