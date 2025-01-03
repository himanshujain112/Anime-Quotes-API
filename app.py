from flask import Flask, request, jsonify
from flask_cors import CORS
import csv
import random
import os

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def index():
    return jsonify({
        "body": "Welcome to Anime Quotes API!",
        "How to use": {
            "/random": "Get a random anime quote",
            "/search?anime=<name>": "Search for quotes by anime name",
            "/search?character=<name>": "Search for quotes by character name"
        },
        "example": {
            "random_quote": "/random",
            "search_anime": "/search?anime=Naruto",
            "search_character": "/search?character=Itachi"
        },
        "Author": "Himanshu Jain",
        "version": "1.0",
        "repository": "https://github.com/himanshujain112/Anime-Quotes-API"
    })

def generateRandom():
    try:
        with open('data/AnimeQuotes.csv', mode='r', encoding="UTF-8") as file:
            reader = list(csv.DictReader(file))
        if reader:
            return random.choice(reader)
        else:
            return {"error": "No quotes available."}
    except Exception as e:
        return {"error": f"Error reading the file: {str(e)}"}

def generateQuote(searchBy=None, query=None):
    results = []
    try:
        with open('data/anime-quotes.csv', mode='r', encoding="UTF-8") as file:
            reader = list(csv.DictReader(file))

        # Search by anime
        if searchBy == "anime" and query:
            for row in reader:
                if query.lower() in row[searchBy].lower():
                    results.append(row)
            if not results:
                return {"error": "No quotes found for the given anime."}

        # Search by character
        elif searchBy == "character" and query:
            for row in reader:
                if query.lower() in row[searchBy].lower():
                    results.append(row)
            if not results:
                return {"error": "No quotes found for the given character."}

        return results

    except Exception as e:
        return {"error": f"Error opening file: {str(e)}"}

@app.route('/random', methods=['GET'])
def generate():
    quote = generateRandom()
    if "error" in quote:
        return jsonify(quote), 400
    return jsonify(quote)

@app.route("/search", methods=['GET'])
def generateBySearch():
    animeQuery = request.args.get("anime")
    characterQuery = request.args.get('character')

    # Ensure only one query parameter is specified
    if animeQuery and characterQuery:
        return jsonify({"error": "Please specify only one search parameter: 'anime' or 'character'."}), 400

    if animeQuery:
        # Search by anime name
        quote = generateQuote('anime', animeQuery)
    elif characterQuery:
        # Search by character name
        quote = generateQuote('character', characterQuery)
    else:
        return jsonify({"error": "Either 'anime' or 'character' parameter is required!"}), 400

    if "error" in quote:
        return jsonify(quote), 404

    return jsonify(quote)

if __name__ == "__main__":
    app.run(debug=False, port=os.environ.get("PORT", 5000))
