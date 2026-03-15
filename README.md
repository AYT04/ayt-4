# 📺 YouTube-to-Mastodon Automator

A collection of Python scripts designed to bridge the gap between your YouTube "Watch Later" list and your Mastodon feed. This project automates the process of sharing content and monitoring channel updates.

## 🚀 What's Inside?

* **`mastodon.py`**: The star of the show. It reads a curated list of YouTube links and periodically shares a random video to your Mastodon followers.
* **`main.py`**: A background monitor that checks specific YouTube RSS feeds every 10 minutes and sends alerts via Discord webhooks when new content drops.
* **`watch_later.txt`**: Your personal library of links used by the bot to decide what to post next.

## 🛠️ Setup

1. **Environment Variables**: Create a `.env` file to store your secrets safely:
* `MASTODON_A_TOKEN`: Your Mastodon access token.
* `DISCORD_WEBHOOK_URL`: Your Discord webhook endpoint.


2. **Configuration**:
* Add your favorite YouTube channel RSS feeds to the `FEEDS` list in `main.py`.
* Dump your "Watch Later" links directly into `watch_later.txt`.



## 🤖 How it Works

The Mastodon script is built for "set it and forget it" automation. It pulls a random link from your text file, formats it into a "toot," and posts it at a regular interval—keeping your social presence active while you’re busy watching the videos yourself.

## 📜 Future Plans

* Support for Matrix and XMPP webhooks.
* Expanded RSS parsing for non-YouTube sources.

---