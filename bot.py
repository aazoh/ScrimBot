import discord
from discord.ext import commands

# Define bot with necessary intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Set the channel IDs where the bot should work
target_channel_ids = [1284150779279577088, 911465862291148844, ]  # Replace with your channel IDs

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    # Check if the message is in one of the specific channels
    if message.channel.id in target_channel_ids and not message.author.bot:
        # Add a reaction to the message
        await message.add_reaction("✅")  # You can change the emoji here
    
    await bot.process_commands(message)  # Process other bot commands

@bot.event
async def on_reaction_add(reaction, user):
    message = reaction.message
    print(f'Reaction added: {reaction.emoji} by {user.name}')

    # Check if the reaction is in a target channel and is the correct reaction
    if message.channel.id in target_channel_ids and str(reaction.emoji) == "✅":
        if user != message.author and not user.bot:  # Ensure the user is not the bot or the message author
            # Send a DM to the message author with the username of the person who reacted
            try:
                await message.author.send(f'{user.name} reacted to your message!')
            except discord.Forbidden:
                print(f"Couldn't send a DM to {message.author}")

            # Delete the original message
            try:
                await message.delete()
                print(f'Deleted message from {message.author.name}')
            except discord.Forbidden:
                print(f"Couldn't delete message from {message.author.name}")

# Run the bot using the token (ensure to keep it secure and private)
bot.run('MTI4NDE1NTg0MDg0NDI3MTY5Nw.GQgd8m.4hZEew8xBWFSDkcOlRKa0VW-f6Khgr2w_odytU')
