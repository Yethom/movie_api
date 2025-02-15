from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import config
from Models.models import Base, Movie, Actor
from get_movies import fetch_popular_movies
from get_actors import fetch_trending_people
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

engine = create_engine(config.DB_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

def save_movies(movies):
    session = Session()
    try:
        for movie in movies:
            new_movie = Movie(
                id=movie["id"],
                title=movie["title"],
                release_date=movie["release_date"],
                overview=movie["overview"],
                ratings=movie["vote_average"]
            )
            session.merge(new_movie)
        session.commit()
    except Exception as e:
        session.rollback()
        logger.error(f"Failed to save movies : {e}")
    finally:
        session.close()

def save_people(actors):
    session = Session()
    try:
        for actor in actors:
            new_actor = Actor(
                id=actor["id"],
                name=actor["name"],
                media_type=actor["media_type"],
                gender=actor["gender"],
                popularity=actor["popularity"]
            )
            session.merge(new_actor)
        session.commit()
    except Exception as e:
        session.rollback()
        logger.error(f"Failed to save actors : {e}")
    finally:
        session.close()

if __name__ == "__main__":
    # movies = fetch_popular_movies()
    # if movies:
    #     save_movies(movies)
    #     print("Success")
    # else:
    #     print("Failed to save movies")

    actors = fetch_trending_people()
    if actors:
        save_people(actors)
        print("Success")
    else:
        print("Failed to save actors")
