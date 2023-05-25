from fastapi import FastAPI
from enum import Enum
app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "restnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name" : model_name, "message":"Deep Learning FTW"}
    if model_name.value == "lenet":
        return {"model_name" : model_name, "message": "LeCNN all the images"}
    return {"model_name" : model_name, "message": "Have some residuals"}

@app.get("/")
async def root():
    return {"message": "Hello World"}
