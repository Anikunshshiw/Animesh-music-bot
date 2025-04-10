from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped

import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client("music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
pytg = PyTgCalls(app)

@app.on_message(filters.command("play") & filters.group)
async def play_music(client, message):
    await pytg.join_group_call(
        message.chat.id,
        AudioPiped("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    )
    await message.reply("Playing music!")

pytg.start()
app.run()
