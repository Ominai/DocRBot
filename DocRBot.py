import os
import textwrap
import discord
import re
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from discord.ext import commands

# Google API Client
credentials = service_account.Credentials.from_service_account_file("GOOGLE_CREDENTIALS.json") # <---- Add Google Credentials.json
drive_api = build("drive", "v3", credentials=credentials)

# Bot Privileges and Prefix
intents = discord.Intents().default()
intents.members = False
intents.voice_states = False
intents.presences = False
intents.guild_messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents) # Can Change Prefix Here

# Reads Google Doc
def docReader(file_id):
    try:
        doc_content = drive_api.files().export(fileId=file_id, mimeType="text/plain").execute()
        return doc_content.decode("utf-8")
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

# Paragraph Formatter
def splitter(content, usernames):
    timestamp = r'(\d{1,2}/\d{1,2}/\d{2,4}) (\d{1,2}:\d{2} (?:AM|PM))'  
    paragraphs = re.split(r'\n\s*\n', content)
    chunks = []

    for paragraph in paragraphs:
        for username in usernames:
            paragraph = paragraph.replace("\n" + username, f"\n{username}")

        # Split timestamp into date and time components
        paragraph = re.sub(timestamp, r'\1 \2', paragraph)

        chunks.append(paragraph)

    return chunks

@bot.command()
async def doc(ctx, file_url):
    print(f"Processing file_url: {file_url}")
    file_id_match = re.search(r"/d/([\w-]+)/", file_url)

    if not file_id_match:
        await ctx.send("Error: Invalid Google Docs URL.")
        return

    file_id = file_id_match.group(1)
    content = docReader(file_id)

    usernames = ["USERNAME", "USERNAME"]  # <------ Add Usernames Here

    if content:
        chunks = splitter(content, usernames)
        for chunk in chunks:
            await ctx.send(chunk)
    else:
        await ctx.send("Error: Could not retrieve the Google Doc content.")

bot.run("BOT_TOKEN") # <------- Add Bot Token Here
