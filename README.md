# Anime Quotes API

Welcome to the **Anime Quotes API**! This API generates random anime quotes and allows you to search for quotes by anime name or character. You can easily integrate this API into your projects or use it to fetch anime quotes for fun.

## Features
- **Get Random Anime Quote**: Fetch a random anime quote from a collection of quotes.
- **Search by Anime**: Retrieve quotes from a specific anime.
- **Search by Character**: Get quotes spoken by a specific character.

## API Endpoints

### 1. Get a Random Anime Quote
**Endpoint**: `/random`

**Method**: `GET`

**Description**: Returns a random anime quote from the database.

**Response Example**:

```json
{
    "quote": "It's not the face that makes someone a monster; it's the choices they make with their lives.",
    "anime": "Naruto",
    "character": "Kakashi Hatake"
}
```

### 2. Search Quotes by Anime
**Endpoint**: `/search?anime=<anime_name>`

**Method**: `GET`

**Description**: Returns all quotes from the specified anime.

**Query Parameters**:

**anime**: The name of the anime to filter by.

**Response Example**:

```json
[
    {
        "quote": "A lesson without pain is meaningless.",
        "anime": "Fullmetal Alchemist",
        "character": "Edward Elric"
    },
    {
        "quote": "The world isn't perfect. But it's there for us, doing the best it can... that's what makes it so damn beautiful.",
        "anime": "Fullmetal Alchemist",
        "character": "Roy Mustang"
    }
]
```

### 3. Search Quotes by Character
**Endpoint**: `/search?character=<character_name>`

**Method**: `GET`

**Description**: Returns all quotes from the specified character.

**Query Parameters**:

**character**: The name of the character to filter by.

**Response Example**:

```json
[
    {
        "quote": "The truth is often painful, but the truth is the only thing that sets us free.",
        "anime": "Naruto",
        "character": "Naruto Uzumaki"
    }
]
```
## Installation

To run this API locally, follow these steps:

### 1. Clone the repository:
```bash
   git clone https://github.com/himanshujain112/Anime-Quotes-API.git
   cd Anime-Quotes-API
```
### 2.Create and activate a virtual environment***:
```bash
  python -m venv venv
  source venv/bin/activate  # For Linux/macOS
  venv\Scripts\activate  # For Windows
```
### 3.Install dependencies:
```bash
  pip install -r requirements.txt
```

### 4. Run the flask app.
```bash
  python app.py
```
*The API will be available at http://127.0.0.1:5000.*

## Deployment
This API is deployed on Vercel for easy access to the endpoints. You can access it at the following URL: (Anime Quotes API on Vercel)[https://anime-quotes-api-seven.vercel.app].

## Contributing
Contributions are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

### Author
Created by [Himanshu Jain](https://github.com/himanshujain112).
