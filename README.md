# Post messages to a Discord server

### Based on https://amunategui.github.io/discord-pager/index.html.

# Setup
Run the following commands to rapid setup:

```bash
git clone git@github.com:usefulcoinengineering/discordmessenger.git
cd discordmessenger
sudo apt install python3-pip
pip3 install requests
sudo timedatectl set-timezone America/Jamaica
python3 main.py
```

Notes:

1. You need to create a server in Discord.
2. Explore server settings to create the webhook.
3. Enter the webhook URL into libraries/constants.py
