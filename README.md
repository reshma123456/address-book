# Address Book FastAPI API

Production‑style FastAPI application for storing addresses and searching nearby locations.

## Features

- Create address
- Update address
- Delete address
- Retrieve addresses within distance
- SQLite database
- SQLAlchemy ORM
- Input validation with Pydantic
- Logging
- Clean architecture

## Setup

Clone repo

git clone https://github.com/reshma123456/address-book.git

cd address-book

Create virtual environment

python -m venv venv

Activate environment

Windows:
venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

OR

python -m pip install -r requirements.txt

Run server

uvicorn app.main:app --reload

Open API docs

http://127.0.0.1:8000/docs