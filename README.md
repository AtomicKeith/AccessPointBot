# AccessPointBot
The current iteration of Prod uses:
* discord.py
* python-dotenv
* yt_dlp
* ffmpeg
To run them you'll need to .env variables; 'prod_token' and 'dev_token' which are both discord bot tokens.

When copying files from dev to prod make sure to change the bot token in 'settings.py', and all of the import paths from 'from dev import x' to 'from prod import x' and the bot prefix in 'main.py'!