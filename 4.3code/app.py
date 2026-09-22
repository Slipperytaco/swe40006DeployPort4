import os # import os to allow for environment variables 
import requests
from flask import Flask

app = Flask(__name__)

# Environment variables required for 4.3 credit task 
APP_NAME = os.getenv("APP_NAME", "Pokemon Lookup App")
APP_ENVIRONMENT = os.getenv("APP_ENVIRONMENT", "development")

@app.route("/")
def home():
    # updated from """ to f""" because python variables are used, we need to add the f 
    return f"""
    <html>
        <head>
            <title>Pokemon Lookup</title>
        </head>
        <body>
            <h1>{APP_NAME}</h1>
            <p>Environment: {APP_ENVIRONMENT}</p>
            <p>Try clicking below for searches:</p>
            <p>Or you can search for any Pokemon by changing the URL for example: /pokemon/pikachu</p>
            <ul>
                <li>
                    <a href="/pokemon/pikachu"> Pikachu</a>
                </li>
                <li>
                    <a href="/pokemon/charizard"> Charizard</a>
                </li>
                <li>
                    <a href="/pokemon/lucario"> Lucario</a>
                </li>
            </ul>
        </body>
    </html> 
    """

@app.route("/pokemon/<name>")
def pokemon(name):
    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{name.lower()}",
        timeout=10
    )

    if response.status_code != 200:
        return f"<h1>Pokemon '{name}' not found</h1>", 404

    data = response.json()

    return f"""
    <html>
        <body>
            <h1>{data['name'].title()}</h1>
            <p>
                <strong>Height:</strong> 
                {data['height']}
            </p>
            <p> 
                <strong>Weight:</strong> 
                {data['weight']}
            </p>
            <p>
                <strong>Base Experience:</strong> {data['base_experience']}
            </p>
            <p>
                <a href="/"> Home</a>
            </p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)