from fastapi import FastAPI, HTTPException
from config import config
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from Models import models

app = FastAPI()

engine = create_engine(config.DB_URL)
SessionLocal = sessionmaker(bind=engine)

# ----- Movies

@app.get("/movies")
def get_movies():
    session = SessionLocal()
    movies = session.query(models.Movie).all()
    session.close()
    if movies:
        return movies
    else:
        raise HTTPException(status_code=404, detail="Movie not found")

@app.get("/movies/{movie_id}")
def get_movie_by_id(movie_id: int):
    session = SessionLocal()
    movies = session.query(models.Movie).filter(models.Movie.id == movie_id).first()
    session.close()
    if movies:
        return movies
    else:
        raise HTTPException(status_code=404, detail=f"Movie with {movie_id=} not found")


@app.delete("/movies/{movie_id}")
def delete_movie_by_id(movie_id: int):
    session = SessionLocal()
    movie = session.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if movie:
        session.delete(movie)
        session.commit()
        return {"message": f"Movie with {movie_id=} deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail=f"Movie with {movie_id=} not found")

# ----- Actors

@app.get("/actors")
def get_actors(gender: int = 0, popularity: float = 0.0):
    session = SessionLocal()
    query = session.query(models.Actor)
    if gender:
        query = query.filter(models.Actor.gender == gender)
    if popularity:
        query = query.filter(models.Actor.popularity >= popularity)

    actors = query.all()
    session.close()
    return actors

@app.delete("/actors/{actor_id}")
def delete_actor_by_id(actor_id: int):
    session = SessionLocal()
    actor = session.query(models.Actor).filter(models.Actor.id == actor_id).first()
    if actor:
        session.delete(actor)
        session.commit()
        return {"message": f"Movie with {actor_id=} deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail=f"Movie with {actor_id=} not found")
