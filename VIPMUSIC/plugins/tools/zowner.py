from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from VIPMUSIC import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


app.on_message(
    filters.command("repo")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b2b2f6136ace5b488c191.jpg",
        caption=f"""ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 👀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐒ᴏᴜʀᴄᴇ", url=f"https://t.me/RadhaSupport")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b2b2f6136ace5b488c191.jpg",
        caption=f"""ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 👀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐒ᴏᴜʀᴄᴇ", url=f"https://t.me/RadhaSupport")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b2b2f6136ace5b488c191.jpg",
        caption=f"""ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 👀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐒ᴏᴜʀᴄᴇ", url=f"https://t.me/RadhaSupport")
                ]
            ]
        ),
    )
