from enum import Enum;
from fastapi import FastAPI;


class ModelName(str, Enum):
  alexnet = "alexnet"
  resnet = "resnet"
  lenet = "lenet"

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
  return {"item_id": item_id}

@app.get("/users/me")
async def current_user_data():
  return {"current user!"}

@app.get("/users/{user}")
async def user_data(user: str):
  return {"user name": user}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
  if model_name is ModelName.alexnet:
    return {"model_name": model_name, "message": "deep learning FTW"}
  if model_name.value == "lenet":
    return {"model_name": model_name, "message": "LeCNN all the images"}
  return {"model_name": model_name, "message": "have some residuals"}