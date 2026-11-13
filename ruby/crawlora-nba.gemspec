require_relative "lib/crawlora/nba/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-nba"
  spec.version = Crawlora::Nba::VERSION
  spec.summary = "NBA API client for Crawlora (70 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted NBA API. Covers games, standings, player and team statistics, play-by-play, and dashboards across 70 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=nba-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-nba", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-nba/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
