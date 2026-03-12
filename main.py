import feedparser
import requests
import time
import os

# Configuration from Environment Variables
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
# List your 4 RSS feed URLs here
FEEDS = [
    "https://www.youtube.com/feeds/videos.xml?channel_id=UCld68syR8Wi-GY_n4CaoJGA",
    "https://www.youtube.com/feeds/videos.xml?channel_id=UCgd5-BWtbgOw5Hx2wP3qxzg",
    "https://www.youtube.com/feeds/videos.xml?channel_id=UCtMVHI3AJD4Qk4hcbZnI9ZQ",
    "https://www.youtube.com/feeds/videos.xml?channel_id=UCs6KfncB4OV6Vug4o_bzijg",
]

# State to remember seen videos so we don't spam
seen_videos = set()

def check_feeds():
    for url in FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            video_id = entry.id
            if video_id not in seen_videos:
                # On first run, it will fill the list without sending
                if seen_videos: 
                    msg = f"{entry.author} uploaded: {entry.link}"
                    requests.post(WEBHOOK_URL, json={"content": msg})
                seen_videos.add(video_id)

while True:
    print("Checking for new videos...")
    check_feeds()
    time.sleep(600)  # Wait 10 minutes before checking again
