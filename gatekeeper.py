import discord
import logging

BOT_TOKEN = '<DISCORD BOT TOKEN>'
SERVER_ID = <SERVER ID>
ROLE_ID = <ROLE ID>
SECRET = 'secret phrase here (all lowercase)'
GREETING = 'Hello! Welcome to the <SERVER NAME> discord server!'

# Set up logging - copied from discord py docs
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Set intents and create bot client
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

# Create message event
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Secret phrase handler
    if message.content.lower() == SECRET:
        role = client.get_guild(SERVER_ID).get_role(ROLE_ID)
        await client.get_guild(SERVER_ID).get_member(message.author.id).add_roles(role)
        logging.info('Executed secret phrase handler...')

@client.event
async def on_member_join(member):
    await member.send(GREETING)
    logging.info('New member joined, sending welcome message...')

client.run(BOT_TOKEN)

