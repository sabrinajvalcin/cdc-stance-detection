import pickle
from pathlib import Path


def save_model(model, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "wb") as file:
        pickle.dump(model, file)


def load_model(model_path):
    with open(model_path, "rb") as file:
        return pickle.load(file)