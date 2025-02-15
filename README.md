# Movie API Project 🎬

## Description
This project is an API to fetch and store information about popular movies and actors. It uses **FastAPI** for managing endpoints and **SQLAlchemy** for the database.

## Technologies Used
- Python
- FastAPI
- SQLAlchemy
- Requests
- PostgreSQL (or any other DBMS compatible with SQLAlchemy)
- Uvicorn (ASGI server)

## Installation

### 1. Clone the Project
```bash
git clone https://github.com/Yethom/movie_api.git
cd movie_api
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Launch the Database (PostgreSQL or other compatible DBMS)
Ensure your database is active and accessible.

### 4. Initialize the DB
```bash
python -c 'from db import Base, engine; Base.metadata.create_all(engine)'
```

### 5. Populate the DB
You can fetch and save popular/treding movies and actors by running the following scripts:
```bash
python get_movies.py  # Fetches and displays popular movies
python get_actors.py  # Fetches and displays popular actors
python db.py  # Saves movies and actors to the database
```
### 6. Start the API
```bash
uvicorn movie_api:app --reload
```
The API will be available at http://127.0.0.1:8000
######
You can also see the docs at http://127.0.0.1:8000/docs

### Available endpoints
#### Movies 
- `GET /movies`: Fetch all movies
- `GET /movies/{movie_id}`: Fetch a specific movie by its ID
- `DELETE /movies/{movie_id}`: Delete a movie
#### Actors
- `GET /actors`: Fetch all actors
- `GET /actors?gender={int}&popularity={float}`: Filter actors by gender and popularity
- `DELETE /actors/{actor_id}`: Delete an actor
