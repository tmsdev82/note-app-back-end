import os
import json

from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import Note

DATA_FILENAME = "notes-data.json"

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sample_data = {
    "title": "This is a test note.",
    "content": "Programming is fun!",
}


def load_notes_data():
    if not os.path.isfile(DATA_FILENAME):
        print("No data found!")
        return []

    with open(DATA_FILENAME, "r") as note_data_file:
        note_data = json.load(note_data_file)
        return note_data


@app.get("/")
async def read_root():
    return sample_data


@app.get("/notes", response_model=List[Note])
async def get_notes():
    return load_notes_data()


@app.post("/notes")
async def add_notes(new_note: Note):

    current_note_data = load_notes_data()
    current_note_data.append(new_note.model_dump())

    with open(DATA_FILENAME, "w") as write_file:
        json.dump(current_note_data, write_file)


@app.delete("/notes/{index}", status_code=204)
async def delete_note(index: int):
    current_note_data = load_notes_data()
    current_note_data.pop(index)

    with open(DATA_FILENAME, "w") as write_file:
        json.dump(current_note_data, write_file)


@app.put("/notes/{index}")
async def update_note(index: int, updated_note: Note):
    current_note_data = load_notes_data()
    current_note_data[index] = updated_note.model_dump()

    with open(DATA_FILENAME, "w") as write_file:
        json.dump(current_note_data, write_file)
