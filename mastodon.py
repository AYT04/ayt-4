import random
from mastodon import Mastodon
from dotenv import load_dotenv
import os
import time

load_dotenv()

# Post interval in seconds (e.g., 3600 = 1 hour)
# Set to 600 to match the 10-minute frequency in main.py
INTERVAL = 600

# Authenticate
mastodon = Mastodon(
    access_token=os.getenv("MASTODON_A_TOKEN"),
    api_base_url='https://mastodon.social'
)

def post_random_video():
    try:
        # Read the YouTube links from the text file
        with open('watch_later.txt', 'r') as f:
            # Filter out empty lines and source markers
            links = [line.strip() for line in f if "youtube.com/watch" in line]
        
        if not links:
            print("No YouTube links found in watch_later.txt")
            return

        video_link = random.choice(links)
        
        toot = f"Check out this video! 📺\n{video_link}"
        
        # Post to Mastodon
        mastodon.status_post(toot)
        print(f"Posted link: {video_link}")
            
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    while True:
        post_random_video()
        time.sleep(INTERVAL)