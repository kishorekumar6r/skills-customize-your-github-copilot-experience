"""
Task Management API - Starter Code
Complete the TODOs to build a REST API with FastAPI
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# TODO: Create FastAPI app instance
app = None

# TODO: Define Pydantic models for Task
# Hint: Create a TaskCreate model with title and description
# Hint: Create a Task model that includes id and completed status


# In-memory storage for tasks
tasks = []
next_id = 1


# TODO: Create root endpoint
# Path: GET /
# Should return: {"message": "Welcome to Task Management API"}


# TODO: Create endpoint to get all tasks
# Path: GET /tasks
# Should return: List of all tasks


# TODO: Create endpoint to get a specific task
# Path: GET /tasks/{task_id}
# Should return: Task with the given ID or 404 error


# TODO: Create endpoint to create a new task
# Path: POST /tasks
# Should accept: TaskCreate model
# Should return: Created task with ID and completed=False


# TODO: Create endpoint to update a task
# Path: PUT /tasks/{task_id}
# Should accept: TaskCreate model
# Should return: Updated task or 404 error


# TODO: Create endpoint to delete a task
# Path: DELETE /tasks/{task_id}
# Should return: Success message or 404 error


if __name__ == "__main__":
    import uvicorn
    # TODO: Run the app using uvicorn
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    pass
