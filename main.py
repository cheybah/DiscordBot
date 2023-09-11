import discord
import os
import random
from discord.ext import commands
from image_downloader import download_known_image  # Import the download function

intents = discord.Intents.default()
intents.typing = True  
intents.message_content = True  # Allow tracking of message content
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def post_image(ctx):
    download_dir = 'downloaded_images'
    
    # List all files in the download directory
    files = os.listdir(download_dir)
    
    # Filter for image files (you can add more supported extensions)
    image_files = [f for f in files if f.endswith(('.jpg', '.png', '.jpeg', '.gif'))]
    
    if image_files:
        # Choose a random image file from the list
        random_image_filename = random.choice(image_files)
        
        # Construct the local file path to the selected image
        local_image_path = os.path.join(download_dir, random_image_filename)
        
        # Send the selected image to the Discord channel
        await ctx.send(file=discord.File(local_image_path))
    else:
        await ctx.send("No images found.")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

bot.run("Your_bot_token")
