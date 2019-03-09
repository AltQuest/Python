tested and working on Linux 16.04 LTS with Python3.6

Reqirements:
  Python3.6
  Discord.py

save DrugWarsBot.py wherevery you will run it from
add your member list like the format of members.txt

Create an app:
Go to https://discordapp.com/developers/applications/me and create a new app. On your app detail page, save the Client ID. You will need it later to authorize your bot for your server.

Create a bot account for your app:
After creating app, on the app details page, scroll down to the section named bot, and create a bot user. Save the token, you will need it later to run the bot.

Authorize the bot for your server:
Visit the URL https://discordapp.com/oauth2/authorize?client_id=XXXXXXXXXXXX&scope=bot but replace XXXX with your app client ID. Choose the server you want to add it to and select authorize.

at this point you should be able to run it:
After running the Python script, your bot should appear online in the server. You can go type !hello to the bot on Discord and it should respond.

help sources: https://www.devdungeon.com/content/make-discord-bot-python
