# FastAPI Notes API

This project is a simple FastAPI-based Notes API that allows you to manage notes. It includes endpoints to create, read, update, and delete notes. The notes data is stored in a JSON file (`notes-data.json`).

For an explanation on how this program was built please see my tutorial [here](https://tms-dev-blog.com/python-and-react-web-app-for-beginners/).

## Features

- **Get all notes**: Retrieve a list of all notes.
- **Add a new note**: Add a new note to the collection.
- **Update a note**: Update an existing note.
- **Delete a note**: Delete a note by its index.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Pydantic

## Installation

1. Clone the repository:

```bash
git clone https://github.com/tmsdev82/note-app-back-end.git
cd note-app-back-end
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate
```

On Windows use :

```
venv\Scripts\activate.bat
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

## Running the application

1. Start the FastAPI application with Uvicorn:

```
uvicorn main:app --reload
```

2. Open your browser and navigate to `http://localhost:8000` to access the API. Or `http://localhost:8000/docs` to see the Swagger UI for the endpoints.
