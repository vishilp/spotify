from app.api import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
#uvicorn main:app --reload
#http://127.0.0.1:8000/
#/docs for default documentation