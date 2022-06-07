from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*",]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {"message": "Hello world"}


@app.get("/users/")
def users_list():
    users = [{"id": i, "name": f"User {i}"} for i in range(1, 11)]
    return users


@app.get("/users/{user_id}")
def user_detail(user_id):
    return {"id": user_id, "username": f"User{user_id}", "name": f"User {user_id}"}


