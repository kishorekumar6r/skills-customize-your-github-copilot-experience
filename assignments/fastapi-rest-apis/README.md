# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern REST APIs using the FastAPI framework. You'll create endpoints, handle different HTTP methods, work with request/response models, and implement proper API design patterns while building a task management API.

## 📝 Tasks

### 🛠️ Set Up FastAPI Project

#### Description
Install FastAPI and create a basic API server with a root endpoint. You'll learn how to structure a FastAPI application, run the development server, and access the automatic interactive API documentation.

#### Requirements
Completed program should:

- Install FastAPI and uvicorn using pip
- Create a FastAPI application instance
- Implement a GET endpoint at the root path (`/`) that returns a welcome message
- Run the server using uvicorn on port 8000
- Access and verify the automatic API documentation at `/docs`


### 🛠️ Create Task Management Endpoints

#### Description
Build a complete CRUD (Create, Read, Update, Delete) API for managing tasks. Each task should have an id, title, description, and completion status. Implement endpoints for all basic operations.

#### Requirements
Completed program should:

- Create a POST endpoint (`/tasks`) to add new tasks with title and description
- Create a GET endpoint (`/tasks`) to retrieve all tasks
- Create a GET endpoint (`/tasks/{task_id}`) to retrieve a specific task by ID
- Create a PUT endpoint (`/tasks/{task_id}`) to update an existing task
- Create a DELETE endpoint (`/tasks/{task_id}`) to remove a task
- Use Pydantic models to validate request and response data
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Store tasks in memory using a Python list or dictionary


### 🛠️ Add Error Handling and Validation

#### Description
Enhance your API with proper error handling and data validation. Implement meaningful error messages when tasks are not found or when invalid data is provided.

#### Requirements
Completed program should:

- Return 404 errors with descriptive messages when a task is not found
- Validate that task titles are not empty and have a maximum length
- Handle duplicate task IDs appropriately
- Use FastAPI's HTTPException for error responses
- Include helpful error messages in all error responses
