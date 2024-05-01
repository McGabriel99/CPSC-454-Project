# CPSC-454-Project

The basis of this project is a University Student Admission Status application. This is where a student can apply for admission, check their status, and withdraw their admission from the university. This application is meant to run on two virtual machines, one hosting the frontend and the other is the backend.

## Installation

For the frontend:

Their is no installation required.

For the backend:

Use the requirements.txt file in the backend folder to install required libraries to run the backend.

```terminal
py -m pip install -r backend/requirements.txt
```

To run the database use the following command.

```bash
uvicorn main:app  --reload --host 0.0.0.0 --port 8000
```

## Usage

To start the
