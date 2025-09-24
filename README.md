# Django
Noting for learning django



# Overview 
Design url --> URLconf
admin --> Create the administrative interface 
models --> where we define our models 
views --> it likes the select in sql 
urls --> create custom url for query 
html --> at view we can return the website, html format for render a website. 
base --> Base like the recycle widget that we can use over and over. 

# Part 1 Request and respone 

    $ django-admin startproject mysite djangotutorial
        Create project mysite in folder djangotutorial

    djangotutorial/
        manage.py
        mysite/
            __init__.py
            settings.py
            urls.py
            asgi.py
            wsgi.py

        Run server 
            python manage.py runserver  --> how to automatic realoading of runserver 
        
        modified files: 
        polls urls.py, views.py 
        mysite urls.py 

# Part 2 Models and admin site 

    $ python manage.py migrate
    $ python manage.py makemigrations polls 
    $ python manage.py sqlmigrate polls 0001
    $ python manage.py shell
        - Where you can send query 
    $ python manage.py createsuperuser 
    $ python manage.py runserver
# Part 3 Views and templates 
    create the templates for rendering the html 
    in views 
# Part 4 Forms and generic views 
    - Forms help you to send to request to you view
    sign it by name and use it 

# Part 5 Testing 
    - Create the automatic testing for your service. 
    - Very important thing 
# Part 6 Static files 
    - Just introduce static file and how to use them in django 
# Part 7 Customizing the admin site 
    - Create the template admin to custom 
    - beside resign we have something like list, fieldset 
# Part 8 Adding third-party packages 
    - There are some package which is created for django 


# Step to create virtual environment for solving the conflict in one machine
    - python3 -m venv venv
    - source venv/bin/activate
    - installation 
    - deactivate 
# Advanced tutorial: How to write reusable apps

    - Package your app: 
        - Name of package: Django-.. module Django_.. 
        - A package can be imported with import foo.bar or from foo import bar. For a directory (like polls) to form a package, it must contain a special file __init__.py, even if this file is empty.
        - Including the files: 
            - README.md (Quick intro,  + quick start)
            - License
            - pyproject.toml: where you define things which need for the project 
            - Manifest define additional files (In this case, it is non-python files)
            - docs(optional) link to online docs
        - python -m build 
    - Install and run: 
        - change mysite/settings.py
        - mysite/urls.py

# Review 

    - First, we create the vitual environment  
        - python3 -m venv venv
        - source venv/bin/activate
        - deactivate 
    - Request and respone 
        - django-admin startproject mysite djangotutorial
        - Difference between app and project ? 
        - python manage.py startapp polls 


# How to deploy django ? 














# AI rewrite 

# 📚 Django Learning Journey

This document serves as my personal reference and summary of key concepts, commands, and best practices for building applications with the Django web framework. It follows the official Django tutorial structure and expands on important topics.

---

## 🚀 The Core of Django

### Project vs. App

-   **Project**: The entire Django application, including settings and configurations. A single project can contain multiple apps.
-   **App**: A modular, reusable component that handles a specific function (e.g., a polls app, a blog app, or a user authentication app).

### The Request-Response Cycle

1.  **URL (`urls.py`)**: Defines URL patterns that map to a view function.
2.  **View (`views.py`)**: Receives a web request and returns a response. It contains the core logic, acting as the "select" in a database query.
3.  **Model (`models.py`)**: Defines the data structure (database tables).
4.  **Template (`.html`)**: The HTML file used by the view to render the final web page. The `base.html` acts as a reusable template for common page elements.

---

## 🛠️ The Django Development Workflow

### 1. Initial Setup & Server Management

-   **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
-   **Start a new project**:
    ```bash
    django-admin startproject mysite .
    ```
-   **Run the development server**:
    ```bash
    python manage.py runserver
    ```

### 2. Models and the Admin Site

-   **Define your models** in `models.py`.
-   **Create migrations** (to track changes to models):
    ```bash
    python manage.py makemigrations <app_name>
    ```
-   **Preview SQL from migrations**:
    ```bash
    python manage.py sqlmigrate <app_name> 0001
    ```
-   **Apply migrations to the database**:
    ```bash
    python manage.py migrate
    ```
-   **Create a superuser** for the admin interface:
    ```bash
    python manage.py createsuperuser
    ```

### 3. Views, URLs, and Templates

-   **Create an app**:
    ```bash
    python manage.py startapp polls
    ```
-   **Create custom URLs**: Configure patterns in `urls.py`.
-   **Create a view**: Write functions in `views.py` that handle requests and return a response, often rendering a template.
-   **Templates**: Create an app-specific `templates` directory to store your HTML files.

---

## 💡 Advanced Topics

### Forms

Forms are a critical part of handling user input and data submission. They manage validation and the overall process of sending data to a view.

### Testing

Testing is a crucial practice in Django development. The built-in testing framework allows you to create automatic tests to ensure your services are reliable and free of bugs.

### Reusable Apps

Packaging an app to be reusable is a Django best practice. This involves:

-   Structuring the app directory as a Python package (containing a `__init__.py` file).
-   Including standard files like `README.md`, `LICENSE`, and `pyproject.toml`.
-   Defining non-Python files (like static files) in a manifest.
-   Using `python -m build` to package the app.

---

## ☁️ Deployment

Preparing a Django project for production involves moving beyond the development server. Key steps include managing static files (`python manage.py collectstatic`) and setting up a production-ready server environment.

---

### **Review Summary**

My core learning flow has been:
1.  **Setup**: Create and activate a virtual environment.
2.  **Project**: Start a Django project.
3.  **App**: Create a separate app for a specific feature.
4.  **Models**: Define the database structure.
5.  **Migrations**: Use `makemigrations` and `migrate`.
6.  **Admin**: Use `createsuperuser` to access the admin site.
7.  **Views & URLs**: Define the core logic and routing.
8.  **Templates**: Create the front-end display.
9.  **Forms**: Handle user input.
10. **Testing**: Implement automated tests.
11. **Static Files**: Manage CSS, JS, and images.
12. **Deployment**: Prepare the project for live use.


