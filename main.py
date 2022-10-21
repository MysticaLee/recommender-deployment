from fastapi import FastAPI, status, HTTPException
from pyBKT.models import Model, Roster
import numpy as np
import re, pickle, os, ast, json


def train_model() -> Model:
    """
    Train a model from some data
    Data is currently hardcoded, but should be loaded from our database or file in the future
    """

    model = Model()
    defaults = {
        "order_id": "Anon Student Id",
        "skill_name": "KC(Default)",
        "correct": "Correct First Attempt",
    }
    model.fit(data_path="Data_Analysis_CSV.csv", defaults=defaults)
    model.save("model-custom.pkl")
    return model


def load_model() -> Model:
    """
    Load a trained model from a pickle file in local storage
    """

    model = Model()
    model.load("model-custom.pkl")
    return model


# Initialize the model (Either load from file or train from some data)
# model = train_model()
model = load_model()

app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
def home() -> dict:
    """
    Homepage
    """

    return {"Status": "The recommender microservice is running!"}