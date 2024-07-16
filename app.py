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
    {"quote": "Fear is not evil. It tells you what your weakness is. And once you know your weakness, you can become stronger as well as kinder.", "character": "Gildarts Clive", "anime": "Fairy Tail"},
    {"quote": "The past makes you want to die out of regret, and the future makes you depressed out of anxiety. So by elimination, the present is likely the happiest time.", "character": "Takasaki Misaki", "anime": "Welcome to NHK"},
    {"quote": "A lesson without pain is meaningless. For you cannot gain something without sacrificing something else in return. But once you have overcome it and made it your own, you will gain an irreplaceable fullmetal heart.", "character": "Edward Elric", "anime": "Fullmetal Alchemist: Brotherhood"},
    {"quote": "I want you to be happy. I want you to laugh a lot. I don’t know what exactly I’ll be able to do for you, but I’ll always be by your side.", "character": "Kagome Higurashi", "anime": "Inuyasha"},
    {"quote": "It’s not the face that makes someone a monster; it’s the choices they make with their lives.", "character": "Naruto Uzumaki", "anime": "Naruto"},
    {"quote": "In our society, letting others find out that you're a nice person is a very risky move. It's extremely likely that someone would take advantage of that.", "character": "Hitagi Senjougahara", "anime": "Bakemonogatari"},
    {"quote": "Power comes in response to a need, not a desire. You have to create that need.", "character": "Goku", "anime": "Dragon Ball Z"},
    {"quote": "We are all like fireworks: we climb, we shine and always go our separate ways and become further apart. But even if that time comes, let’s not disappear like a firework, and continue to shine forever.", "character": "Hitsugaya Toshiro", "anime": "Bleach"},
    {"quote": "If you don’t take risks, you can’t create a future.", "character": "Monkey D. Luffy", "anime": "One Piece"},
    {"quote": "Sometimes, we have to look beyond what we want and do what's best.", "character": "Kakashi Hatake", "anime": "Naruto"},
    {"quote": "The world is cruel, but also very beautiful.", "character": "Mikasa Ackerman", "anime": "Attack on Titan"},
    {"quote": "To know sorrow is not terrifying. What is terrifying is to know you can't go back to happiness you could have.", "character": "Matsumoto Rangiku", "anime": "Bleach"},
    {"quote": "A person grows up when he's able to overcome hardships. Protection is important, but there are some things that a person must learn on his own.", "character": "Jiraiya", "anime": "Naruto"},
    {"quote": "You can't sit around envying other people's worlds. You have to go out and change your own.", "character": "Shinichi Kudo", "anime": "Detective Conan"},
    {"quote": "The only thing we're allowed to do is to believe that we won't regret the choice we made.", "character": "Levi Ackerman", "anime": "Attack on Titan"},
    {"quote": "The moment you think of giving up, think of the reason why you held on so long.", "character": "Natsu Dragneel", "anime": "Fairy Tail"},
    {"quote": "Forgetting is like a wound. The wound may heal, but it has already left a scar.", "character": "Monkey D. Luffy", "anime": "One Piece"},
    {"quote": "It is not the face that makes someone a monster; it is the choices they make with their lives.", "character": "Naruto Uzumaki", "anime": "Naruto"},
    {"quote": "Sometimes, we have to look beyond what we want and do what's best.", "character": "Kakashi Hatake", "anime": "Naruto"},
    {"quote": "You can't sit around envying other people's worlds. You have to go out and change your own.", "character": "Shinichi Kudo", "anime": "Detective Conan"},
    {"quote": "Sometimes, we have to look beyond what we want and do what's best.", "character": "Kakashi Hatake", "anime": "Naruto"},
    {"quote": "The world is cruel, but also very beautiful.", "character": "Mikasa Ackerman", "anime": "Attack on Titan"},
    {"quote": "The only thing we're allowed to do is to believe that we won't regret the choice we made.", "character": "Levi Ackerman", "anime": "Attack on Titan"},
    {"quote": "The moment you think of giving up, think of the reason why you held on so long.", "character": "Natsu Dragneel", "anime": "Fairy Tail"},
    {"quote": "A lesson without pain is meaningless. For you cannot gain something without sacrificing something else in return. But once you have overcome it and made it your own, you will gain an irreplaceable fullmetal heart.", "character": "Edward Elric", "anime": "Fullmetal Alchemist: Brotherhood"},
    {"quote": "Fear is not evil. It tells you what your weakness is. And once you know your weakness, you can become stronger as well as kinder.", "character": "Gildarts Clive", "anime": "Fairy Tail"},
    {"quote": "I don't want to run away anymore. I don't want to lie to myself anymore.", "character": "Shinji Ikari", "anime": "Neon Genesis Evangelion"},
    {"quote": "I'm not stupid. I'm just too lazy to show how smart I am.", "character": "Oreki Houtarou", "anime": "Hyouka"},
    {"quote": "The world's not perfect, but it's there for us trying the best it can. That's what makes it so damn beautiful.", "character": "Roy Mustang", "anime": "Fullmetal Alchemist: Brotherhood"},
    {"quote": "If you wanna make people dream, you've gotta start by believing in that dream yourself!", "character": "Simon", "anime": "Gurren Lagann"},
    {"quote": "No matter how deep the night, it always turns to day, eventually.", "character": "Brook", "anime": "One Piece"},
    {"quote": "You should enjoy the little detours. To the fullest. Because that's where you'll find the things more important than what you want.", "character": "Ging Freecss", "anime": "Hunter x Hunter"},
    {"quote": "I don't want to swim. I don't want to be free. I just want to stay here and decay.", "character": "Rei Ayanami", "anime": "Neon Genesis Evangelion"},
    {"quote": "People's lives don't end when they die, it ends when they lose faith.", "character": "Itachi Uchiha", "anime": "Naruto"},
    {"quote": "Whatever you lose, you'll find it again. But what you throw away you'll never get back.", "character": "Kenshin Himura",
]

@app.route('anime/quote', methods=['GET'])
def get_random_anime_quote():
    return jsonify(random.choice(anime_quotes))

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    keep_alive()
