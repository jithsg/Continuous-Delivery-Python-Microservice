from fastapi import FastAPI
from mylib.logic import wiki as wiki_logic
from mylib.logic import search as search_logic


app = FastAPI()

@app.get("/")
async def root():
    return {"Wikipedia API": "Welcome to the Wikipedia API"}

@app.get("/wiki/{name}")
async def wiki(name: str):
    """Return a summary from Wikipedia."""
    result = wiki_logic(name)
    return {"result": result}

@app.get("/search/{name}")
async def search(name: str):
    """Return a list of Wikipedia search results."""
    result = search_logic(name)
    return {"result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)