from fastapi import FastAPI
from rec import recommend_songs


# Initialize FastAPI
app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to the Music Recommendation API"}

@app.get("/recommend")
def rec_songs(song_name: str, top_n: int = 5):
    print(song_name)
    recommendations = recommend_songs(song=song_name, num_rec=top_n) 
    return {
        "recommendations":[recommendations['name']]
    }
    
# query template:
# http://127.0.0.1:8000/recommend?song_name=Shape%20of%20You&top_n=5