# Take-Home-Challenge---Hatio
 
# Todo Management Project
## Overview
Welcome to the Todo Management Project! This Django application allows users to manage tasks (todos) within projects. Features include creating, updating, deleting projects and todos, managing todo status while updating the task, and exporting project summaries as GitHub Gists in Markdown format.

## Features
User Authentication: Register, login, and manage user accounts.

Project Management: Create, edit, and delete projects.

Todo Management: Add, update, delete, and mark todos as completed or pending.

Status Updates: Change todo status directly from the homepage.

Summary Export: Generate and export project summaries as GitHub Gists in Markdown format.

## Installation
## Prerequisites
Ensure you have the following installed:

Python 3.x

Django 3.x or higher

A GitHub Token (for exporting Gists)


## Setup
 1. Clone the Repository
git clone https://github.com/yourusername/todo-management-project.git
cd todo-management-project

 2. Create and Activate a Virtual Environment
python -m venv venv

 3. Install Dependencies
pip install -r requirements.txt

 4. Apply Database Migrations
python manage.py migrate

**Create a New Migration:** If you make changes to models, create new migrations:
 python manage.py makemigrations
 
 **Apply New Migrations:** Apply any new migrations:
 python manage.py migrate
 
 5. Create a Superuser (Optional, for admin access)
python manage.py createsuperuser

## Running the Application
 1. Start the Development Server
python manage.py runserver

 2. Open the Application
Navigate to http://127.0.0.1:8000/ in your web browser.

**Stop the Server:** Press Ctrl + C in the command prompt where the server is running.


## Usage
Home Page: View a list of projects. Click on a project to see its details and todos.

Project Details: View, edit, and delete projects. Add todos to the project.

Todos: Mark todos as completed or pending directly from the home page. Update or delete todos as needed.

Export Summary: Click the "Export as Gist" button on the project details page to export the project summary as a GitHub Gist.


## URL Patterns
Here are the key routes available in the application:

 1. `/` - Home Page: View all projects and todos.
 2. `/login/` - Login Page: User login.
 3. `/logout/` - Logout: End the current user session.
 4. `/register/` - Registration Page: Create a new user account.
 5. `/project/new/` - Create Project: Create a new project.
 6. `/todo/delete/<int:pk>/` - Delete Project: Remove a project.
 7. `/view_project/<int:project_id>/` - Project Details: View details of a specific project.
 8. `/edit_project_title/<int:project_id>/` - Edit Project Title: Change the title of a project.
 9. `/todo/new/<int:project_id>/` - Create Todo: Add a new todo to a project.
 10. `/todo/update/<int:pk>/` - Update Todo: Modify an existing todo.
 11. `/todo/delete/<int:pk>/` - Delete Todo: Remove a todo.
 12. `/todo/<int:pk>/` - Todo Details: View details of a specific task.
 13. `/project/export/<int:project_id>/` - Export Project Summary as Gist: Generate and export a project summary in Markdown format.


## Contributing
We welcome contributions to improve the project. To contribute:

 1. Fork the repository.
 2. Create a new branch (git checkout -b feature-branch).
 3. Make your changes.
 4. Commit your changes (git commit -am 'Add new feature').
 5. Push your branch (git push origin feature-branch).
 6. Open a Pull Request.


## Acknowledgments
**Django:** The primary framework used for building this application. Django is a high-level Python web framework that encourages rapid development and clean, practical design.

**GitHub:** For hosting the project repository and for Gist API integration, which allows exporting project summaries. GitHub provides a platform for version control and collaboration
