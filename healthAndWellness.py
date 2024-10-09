import discord
import asyncio
import random

# Define the intents for the bot
intents = discord.Intents.default()
intents.messages = True  # Allow the bot to send messages

# Create the bot instance
client = discord.Client(intents=intents)

# List of reminders
reminders = [
    "Drink water 💧",
    "Take a deep breath 🌬️",
    "Stretch your legs 🦵",
    "Check your posture 🧘",
    "Take a short break ⏳",
    "Blink and relax your eyes 👁️",
]

# Function to send random reminders periodically
async def send_reminders(channel):
    while True:
        # Pick a random reminder
        reminder = random.choice(reminders)
        await channel.send(reminder)
        # Wait for a specified time before sending the next reminder (e.g., 1 hour)
        await asyncio.sleep(3600)  # Sleep for 3600 seconds (1 hour)

# Event that runs when the bot is ready
@client.event
async def on_ready():
    print(f'Bot {client.user} is connected and ready to send reminders!')
    
    # Specify the channel to send reminders to by name
    channel = discord.utils.get(client.get_all_channels(), name='general')  # Change 'general' to your channel name
    if channel:
        await send_reminders(channel)

# Run the bot with token (not actually put in order to protect token)
client.run('discordBotTokenHere')
