import asyncio
import random
import os
from pyrogram import Client
from pyrogram.enums import ParseMode
from flask import Flask
import threading
from dotenv import load_dotenv

# Load secrets from .env or Railway environment
load_dotenv()
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
STRING_SESSION = os.getenv("STRING_SESSION")
TARGET_CHAT = "@MoviesandSeries36"

movies = [
    # Hollywood
    "John Wick 2014", "John Wick Chapter 2", "John Wick Chapter 3", "John Wick Chapter 4",
    "Inception 2010", "Avengers Endgame 2019", "The Dark Knight 2008", "Interstellar 2014",
    "Avatar 2009", "Iron Man 2008", "Doctor Strange 2022", "Deadpool 2016",
    "Tenet 2020", "Oppenheimer 2023", "Dune 2021", "Fight Club 1999", "The Matrix 1999",
    "Gladiator 2000", "No Time To Die 2021", "The Batman 2022", "Fast X 2023",
    "Spider-Man No Way Home 2021", "The Meg 2 2023", "Transformers Rise of the Beasts",
    "The Flash 2023", "The Equalizer 3", "Extraction 2", "The Marvels 2023",
    "Black Panther Wakanda Forever", "The Whale 2022", "The Menu 2022", "Fall 2022",
    "Bullet Train 2022", "Prey 2022", "Jungle Cruise", "The Suicide Squad 2021",
    "Knives Out 2019", "Glass Onion 2022", "Mortal Kombat 2021", "Ready Player One",
    "Alita Battle Angel", "Logan 2017", "The Wolverine 2013", "X-Men Days of Future Past",
    "The Hunger Games", "Now You See Me", "Oblivion 2013", "Edge of Tomorrow",
    # Hindi
    "Pathaan 2023", "Jawaan 2023", "War 2019", "RRR 2022", "Gadar 2 2023",
    "Shershaah 2021", "Animal 2023", "Brahmastra 2022", "Dhamaka 2021",
    # Tamil
    "Leo 2023", "Master 2021", "Vikram 2022", "Beast 2022", "Jailer 2023",
    "Doctor 2021", "Maaveeran 2023", "Thunivu 2023"
]

# Userbot client using string session
app = Client(
    name="userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION,
    parse_mode=ParseMode.HTML
)

# Flask Web Server for Railway uptime
web_app = Flask("")

@web_app.route("/")
def home():
    return "Userbot is running!"

def run_flask():
    web_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

async def spam_movies():
    async with app:
        print("Userbot started. Sending movie names every 8 minutes...")
        while True:
            movie = random.choice(movies)
            try:
                await app.send_message(TARGET_CHAT, movie)
                print(f"Sent: {movie}")
            except Exception as e:
                print(f"Error: {e}")
            await asyncio.sleep(480)  # 8 minutes

def main():
    threading.Thread(target=run_flask).start()
    asyncio.run(spam_movies())

if __name__ == "__main__":
    main()￼Enter
