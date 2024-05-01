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

To run the database use the following command in the backend folder on bash.

```bash
uvicorn main:app  --reload --host 0.0.0.0 --port 8000
```

## Usage

Before starting up the frontend, replace the fetch lines 69, 84, 100 from:

```javascript
http://localhost:8000/apply/
```

To:

```javascript
http://yourIPAddress:8000/apply/
```

Replace the yourIPAddress with your actual IP address of the backend virtual machine that host the database.

Once replaced, start up the backend with the uvicorn command above, and then startup the frontend as well.

To change between either light/dark mode, click on the button of your choice.

To Apply for University Admission, enter a student id, any amount of numbers, and a student name, any name length. Once filled out, click on the Apply for University and if you check on the applications.db file on the backend virtual machine, you should see it should update and have the student id, name, and status in the database.

To get the status of a student, enter a student id in the 'Enter Student ID' field. Once filled out, click on 'Get Status' and in the 'Status Result' section should appear the student id as well as the students status.

To change a student's status to withdrawn, enter a student id in the 'Withdraw from University' field and then click on the 'Withdraw Application' button. Once clicked on, the 'Status Result' should display the student id as well as the new student status which is 'withdrawn'.
