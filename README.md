# Mini Project 4 - Task Manager Django Web Application

**Author:** Brian Shoemaker  
**Course:** 2025F INF601 A Advanced Programming with Python  
**Project:** Mini Project 4

## Description

This is a Django-based task management web application that allows users to create, manage, and track their tasks. 
The application features user authentication, task CRUD operations, priority and status management, and a responsive 
Bootstrap interface.

## Features

- **User Authentication**: Register, login, and logout functionality
- **Task Management**: Create, view, edit, and delete tasks
- **Task Properties**:
  - Title and description
  - Priority levels (Low, Medium, High)
  - Status tracking (Pending, In Progress, Completed)
  - Due dates
- **Bootstrap UI**: Clean, responsive interface with Bootstrap 5
- **Bootstrap Modal**: Information modal on the home page
- **Django Admin**: Full admin panel with customized Task model display
- **User-specific Tasks**: Each user can only see and manage their own tasks

## Pages

The application includes the following pages:
1. **Home Page** (`/`) - Landing page with information modal
2. **Task List** (`/tasks/`) - Display all user's tasks
3. **Task Detail** (`/task/<id>/`) - View detailed information about a task
4. **Create Task** (`/task/new/`) - Form to create a new task
5. **Edit Task** (`/task/<id>/edit/`) - Form to edit an existing task
6. **Delete Task** (`/task/<id>/delete/`) - Confirmation page to delete a task
7. **Login** (`/login/`) - User login page
8. **Register** (`/register/`) - User registration page

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone or download the project files**

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Initialize the database**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create your admin account.

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the application**:
   - Open your web browser and go to: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Usage

### Creating Your First Task

1. Register a new account or login with existing credentials
2. Click on "New Task" in the navigation bar or from the home page
3. Fill in the task details:
   - Title (required)
   - Description (optional)
   - Priority (Low, Medium, or High)
   - Status (Pending, In Progress, or Completed)
   - Due Date (optional)
4. Click "Create Task" to save

### Managing Tasks

- **View all tasks**: Click on "My Tasks" in the navigation
- **View task details**: Click the "View" button on any task card
- **Edit a task**: Click the "Edit" button and update the information
- **Delete a task**: Click the "Delete" button and confirm the deletion
- **Use the modal**: On the home page, click "Learn More" to see feature details

### Admin Panel

The Django admin panel provides advanced task management capabilities:
1. Log in at `/admin/` with your superuser credentials
2. View all tasks with custom list display showing priority, status, and dates
3. Filter tasks by priority, status, and creation date
4. Search tasks by title and description
5. Edit tasks with organized fieldsets

## Project Structure

```
miniproject4/
├── manage.py                      # Django management script
├── requirements.txt               # Python dependencies
├── README.md                      # This file
├── miniproject4/                  # Project configuration
│   ├── __init__.py
│   ├── settings.py               # Project settings
│   ├── urls.py                   # Main URL configuration
│   └── wsgi.py                   # WSGI configuration
└── tasks/                        # Tasks application
    ├── __init__.py
    ├── admin.py                  # Admin configuration
    ├── apps.py                   # App configuration
    ├── forms.py                  # Django forms
    ├── models.py                 # Database models
    ├── views.py                  # View functions
    ├── urls.py                   # App URL patterns
    ├── migrations/               # Database migrations
    └── templates/                # HTML templates
        └── tasks/
            ├── base.html         # Base template with Bootstrap
            ├── home.html         # Home page
            ├── task_list.html    # Task list page
            ├── task_detail.html  # Task detail page
            ├── task_form.html    # Create/edit task form
            ├── task_confirm_delete.html  # Delete confirmation
            ├── login.html        # Login page
            └── register.html     # Registration page
```

## Technologies Used

- **Django 5.1.3**: Web framework
- **Python 3.x**: Programming language
- **SQLite**: Database (default Django database)
- **Bootstrap 5.3.0**: Frontend framework
- **Bootstrap Icons**: Icon library

## Database Models

### Task Model
- `title`: CharField (max 200 characters)
- `description`: TextField (optional)
- `priority`: CharField with choices (low, medium, high)
- `status`: CharField with choices (pending, in_progress, completed)
- `due_date`: DateTimeField (optional)
- `created_at`: DateTimeField (auto-generated)
- `updated_at`: DateTimeField (auto-updated)
- `user`: ForeignKey to User model

## Notes for Grading

- ✅ Initial comments with name, class, and project in all Python files
- ✅ Proper import of packages
- ✅ Django folder structure with one app (tasks)
- ✅ Minimum of 5 pages (8 pages total)
- ✅ Proper template structure with base template
- ✅ Form usage (TaskForm and UserRegisterForm)
- ✅ Django admin setup with custom styling
- ✅ Bootstrap integration in all templates
- ✅ Bootstrap modal on home page
- ✅ Register and login system implemented
- ✅ Requirements.txt file included
- ✅ README.md with detailed instructions

## Git Workflow

To create the required 5+ commits:

```bash
# Initial commit
git init
git add manage.py miniproject4/ tasks/models.py tasks/admin.py
git commit -m "Initial Django project setup with Task model and admin"

# Second commit
git add tasks/forms.py tasks/views.py tasks/urls.py
git commit -m "Add forms and views for task management"

# Third commit
git add tasks/templates/
git commit -m "Add HTML templates with Bootstrap styling"

# Fourth commit
git add requirements.txt README.md
git commit -m "Add requirements.txt and comprehensive README"

# Fifth commit
git add .
git commit -m "Final project polish and documentation"
```

## Troubleshooting

### Common Issues

1. **Module not found error**: Make sure you've activated your virtual environment and installed all requirements
2. **Database errors**: Run migrations with `python manage.py migrate`
3. **Static files not loading**: Run `python manage.py collectstatic` (for production)
4. **Port already in use**: Specify a different port: `python manage.py runserver 8080`

## License

This project is created for educational purposes as part of INF601 coursework.

## Contact

For questions or issues, please contact the instructor via email as specified in the project requirements.