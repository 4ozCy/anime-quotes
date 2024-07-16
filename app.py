from flask import Flask, jsonify
from threading import Thread
import random

app = Flask(__name__)

anime_quotes = [
    {"quote": "The only ones who should kill are those prepared to be killed.", "character": "Lelouch Lamperouge", "anime": "Code Geass"},
    {"quote": "I don't want to conquer anything. I just think the guy with the most freedom in this whole ocean... is the Pirate King!", "character": "Monkey D. Luffy", "anime": "One Piece"},
    {"quote": "Whatever you lose, you'll find it again. But what you throw away you'll never get back.", "character": "Kenshin Himura", "anime": "Rurouni Kenshin"},
    {"quote": "People's lives don't end when they die, it ends when they lose faith.", "character": "Itachi Uchiha", "anime": "Naruto"},
    {"quote": "I don't want to swim. I don't want to be free. I just want to stay here and decay.", "character": "Rei Ayanami", "anime": "Neon Genesis Evangelion"},
    {"quote": "You should enjoy the little detours. To the fullest. Because that's where you'll find the things more important than what you want.", "character": "Ging Freecss", "anime": "Hunter x Hunter"},
    {"quote": "No matter how deep the night, it always turns to day, eventually.", "character": "Brook", "anime": "One Piece"},
    {"quote": "If you wanna make people dream, you've gotta start by believing in that dream yourself!", "character": "Simon", "anime": "Gurren Lagann"},
    {"quote": "The world's not perfect, but it's there for us trying the best it can. That's what makes it so damn beautiful.", "character": "Roy Mustang", "anime": "Fullmetal Alchemist: Brotherhood"},
    {"quote": "I'm not stupid. I'm just too lazy to show how smart I am.", "character": "Oreki Houtarou", "anime": "Hyouka"},
    {"quote": "I don't want to run away anymore. I don't want to lie to myself anymore.", "character": "Shinji Ikari", "anime": "Neon Genesis Evangelion"},
    {"quote": "People's lives don't end when they die. It ends when they lose faith.", "character": "Itachi Uchiha", "anime": "Naruto"},
    {"quote": "Fear is not evil. It tells you what your weakness is. And once you know your weakness, you can become stronger as well as kinder.", "character": "Gildarts Clive", "anime": "Fairy Tail"},
    {"quote": "People's lives don't end when they die, it ends when they lose faith.", "character": "Itachi Uchiha", "anime": "Naruto"},
    {"quote": "The past makes you want to die out of regret, and the future makes you depressed out of anxiety. So by elimination, the present is likely the happiest time.", "character": "Takasaki Misaki", "anime": "Welcome to NHK"},
]

@app.route('/api/anime/quote', methods=['GET'])
def get_random_anime_quote():
    return jsonify(random.choice(anime_quotes))

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    keep_alive()
