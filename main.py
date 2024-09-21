from fastapi import Body, FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to my FastAPI server!!!"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your first post!"}


@app.post("/createposts")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"message": "Successfully created a new post"}
    