use crawlora_nba::{Client, NbaGamesParams, serde_json};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .nba
        .games(Default::default())
        .await?;
    let data: serde_json::Value = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
