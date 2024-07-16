from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

def load_quotes():
    with open('quotes.json', 'r') as file:
        return json.load(file)

quotes = load_quotes()

@app.route('/api/quote', methods=['GET'])
def get_random_quote():
    return jsonify(random.choice(quotes))

if __name__ == '__main__':
    app.run(port=8000)
