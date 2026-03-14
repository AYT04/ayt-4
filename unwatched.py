import feedparser
import requests
import time
import os

# Configuration from Environment Variables
WEBHOOK_URL = os.getenv("unwatched_DISCORD_WEBHOOK_URL")
CHANNELS_FILE = "watch_later.txt"

# State to remember seen videos so we don't spam
seen_videos = set()

def load_feeds():
    """Reads the RSS feed URLs from the channels.txt file."""
    if not os.path.exists(CHANNELS_FILE):
        print(f"Error: {CHANNELS_FILE} not found.")
        return []
    
    with open(CHANNELS_FILE, "r") as f:
        # Read lines, strip whitespace, and ignore empty lines
        return [line.strip() for line in f if line.strip()]

def check_feeds():
    feeds = load_feeds()
    if not feeds:
        print("No feeds found to check.")
        return

    for url in feeds:
        try:
            feed = feedparser.parse(url)
            # Handle potential feed parsing errors
            if feed.bozo:
                continue

            for entry in feed.entries:
                video_id = entry.id
                if video_id not in seen_videos:
                    # On first run, it will fill the list without sending
                    if seen_videos: 
                        author = getattr(entry, 'author', 'Unknown Creator')
                        msg = f"{author} uploaded: {entry.link}"
                        requests.post(WEBHOOK_URL, json={"content": msg})
                    seen_videos.add(video_id)
        except Exception as e:
            print(f"Error checking feed {url}: {e}")

if __name__ == "__main__":
    if not WEBHOOK_URL:
        print("Error: DISCORD_WEBHOOK_URL environment variable is not set.")
    else:
        print(f"Bot started. Monitoring {CHANNELS_FILE}...")
        while True:
            print(f"Checking {len(load_feeds())} feeds for new videos...")
            check_feeds()
            time.sleep(600)