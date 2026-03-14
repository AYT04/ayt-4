# 🚀 ayt-4: The Ultimate YT-to-Discord Plug

No cap, staying on top of your favorite creators is a whole mood, but checking YouTube every five minutes is not it. `ayt-4` is a lightweight, high-key efficient Python bot that stalk—uh, *monitors*—your favorite channels and pings your Discord server the second they drop new heat.

## ✨ Why it Slays

* **Real-Time Vibes:** Refreshes every 10 minutes so you’re never late to the comment section.
* **Multi-Channel Energy:** Tracks up to 4 different RSS feeds simultaneously (standard setup).
* **Zero Spam Policy:** Smart state management ensures you only get notified once per upload—we don't do that double-posting mess.
* **Clean Code:** Written in Python using `feedparser` and `requests` for that buttery smooth performance.

## 🛠️ The Tech Stack

* **Python 3.x** (The blueprint)
* **feedparser** (To read the tea)
* **requests** (To send it to Discord)

## 📥 Getting Started (Tutorial Core)

1. **Clone the Repo**
```bash
git clone https://github.com/AYT04/ayt-4.git
cd ayt-4

```


2. **Install Dependencies**
Don't be a local, install the requirements:
```bash
pip install -r requirements.txt

```


3. **Set Your Environment Variables**
You need to feed the bot your Discord Webhook URL. It’s giving security:
```bash
export DISCORD_WEBHOOK_URL='your_webhook_link_here'

```


4. **Launch 🚀**
```bash
python main.py

```



## ⚙️ Configuration

Wanna change the channels? Just hop into `main.py` and swap the URLs in the `FEEDS` list. Currently tracking some absolute legends, but you can make it your own.

## 📜 The Fine Print

This project is licensed under the **GNU General Public License v3.0**. Basically, keep it open, keep it free, and don't be a gatekeeper. Check the `LICENSE` file for the full lore.

---

*Maintained with main character energy.* 💅
