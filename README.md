This is a very specific use-case bit of code for a Discord Bot that reads a Google Doc link you have access to that holds Discord Formatted Messages, then posts those messages back into Discord post-by-post.  

You will need to set up a few things to get the bot working correctly:

Python:
 ---Checking for Python:
1. Press the "Windows" key on your keyboard and type "cmd" into the search box.
2. Click on the "Command Prompt" app to open it.
3. Type "python" into the command prompt and press enter.
If Python is installed, you will see the version number displayed. If Python is not installed, you will receive an error message.
 ---Installing Python:
1. Go to the Python website at https://www.python.org/downloads/ in your web browser.
2. Click on the "Download" button for the latest version of Python.
3. Choose the Windows installer for your system. If you are unsure, check the "System type" information in the System Properties window (accessible by right-clicking on "This PC" or "My Computer" and selecting "Properties").
4. Run the installer and select the "Add Python to PATH" option. This will add Python to your system's PATH environment variable, allowing you to run Python from the command prompt or terminal.
5. Click the "Install Now" button to start the installation process.
6. Wait for the installation to complete, then click "Close".
7. Open the terminal again and type 'python'. If you see a version number you've installed python.

Google Credentials File:
1. Go to the Google Cloud Console at https://console.cloud.google.com/.
2. Create a new project by clicking on the project dropdown menu in the top navigation bar and selecting "New Project". Enter a name for your project and click "Create".
3. In the left sidebar, click on "APIs & Services" and then "Dashboard".
4. Click on the "+ ENABLE APIS AND SERVICES" button at the top of the page and search for "Google Drive API" and "Google Docs API". Click on each of them to enable them for your project.
5. In the left sidebar, click on "APIs & Services" and then "Credentials".
6. Click on the "+ CREATE CREDENTIALS" button and select "Service account".
7. Fill in the necessary fields, including the service account name and ID, and select a role for the service account. For the Google Drive and Google Docs APIs, you will need to assign the "Project" > "Editor" role to the service account.
8. Click on "Create" to create the service account.
9. On the next screen, you will be prompted to create a new key for the service account. Click on the "Create key" button and select the "JSON" key type.
10. The JSON key file will be downloaded to your computer. Put the .json into the DocRBot folder.

Discord Bot Token:
1. Go to the Discord Developer Portal website (https://discord.com/developers/applications) and log in with your Discord account.
2. Click on the "New Application" button and give your application a name. This will be the name of your Discord bot.
3. Click on the "Bot" tab on the left-hand side menu and then click on the "Add Bot" button. Confirm that you want to add a bot.
4. Under the "Privileged Gateway Intents" section, enable the intents that your bot will need. Turn on all three.
5. Once you've enabled the necessary intents, scroll up to the "Token" section and click on the "Copy" button.

Setting Up the Bot:
1. Download and use Notepad++ (https://notepad-plus-plus.org/) to open DocRBot.py
2. Replace GOOGLE_CREDENTIALS.json with the name of .json file you downloaded from Google
3. Scroll down and change the Usernames to the Usernames found in your Google Doc File. Add more as needed.
4. Replace BOT_TOKEN with the Discord Bot Token.

Inviting the Bot:
1. First, go to the Discord Developer Portal and select your bot application.
2. Click on the "OAuth2" tab from the left-hand side menu.
3. In the "Scopes" section, select "bot".
4. Scroll down and select the permissions you want your bot to have. These permissions determine what actions your bot can perform on your server, such as sending messages, managing roles, or kicking members.
5. Once you've selected the permissions you want your bot to have, a link will be generated in the "Scopes" section.
6. Click on the generated link to invite your bot to your server.
7. On the authorization screen, select the server you want to invite the bot to, and click "Authorize".
8. If the authorization is successful, your bot should appear in your server's member list.

Activating the Bot:
1. Open the terminal.
2. Type 'cd' and drag the DocRBot folder into the terminal and press enter.
3. You're now in the DocRBot Directory. Type 'python DocRBot.py' (case-sensitive)
4. The bot should now be online! Assuming you didn't change the prefix, type '!doc' and add the URL of the document you want to copy into Discord. Be aware that it will post in the same channel you called the command.
5. If the bot has any problems with the document it is likely that it doesn't have permission to view it. 
