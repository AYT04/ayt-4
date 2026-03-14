import feedparser
import random
from mastodon import Mastodon
from dotenv import load_dotenv
import os

load_dotenv()

# Authenticate
mastodon = Mastodon(
    access_token=os.getenv("MASTODON_A_TOKEN"),
    api_base_url='https://mastodon.social'
)

# Read RSS feed URLs
with open('watch_later.txt', 'r') as f:
    feeds = [line.strip() for line in f if line.strip()]

# Pick random feed and get latest video
feed_url = random.choice(feeds)
feed = feedparser.parse(feed_url)

if feed.entries:
    latest = feed.entries[0]
    toot = f"New video: {latest.title} 📺\n{latest.link}"
    mastodon.status_post(toot)