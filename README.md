# Django
Noting for learning django


`
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

        
    - python -m build
    - python -m pip install --user django-polls/dist/django_polls-0.1.tar.gz

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



# Model 

  - Relationship: 
    - One to many use ForeignKey in one 
    - Many to Many: ManyToManyField (Using through like in chatting)
    ```bash
      >>> ringo = Person.objects.create(name="Ringo Starr")
      >>> paul = Person.objects.create(name="Paul McCartney")
      >>> beatles = Group.objects.create(name="The Beatles")
      >>> m1 = Membership(
      ...     person=ringo,
      ...     group=beatles,
      ...     date_joined=date(1962, 8, 16),
      ...     invite_reason="Needed a new drummer.",
      ... )
      >>> m1.save()
      >>> beatles.members.all()
      <QuerySet [<Person: Ringo Starr>]>
      >>> ringo.group_set.all()
      <QuerySet [<Group: The Beatles>]>
      >>> m2 = Membership.objects.create(
      ...     person=paul,
      ...     group=beatles,
      ...     date_joined=date(1960, 8, 1),
      ...     invite_reason="Wanted to form a band.",
      ... )
      >>> beatles.members.all()
      <QuerySet [<Person: Ringo Starr>, <Person: Paul McCartney>]>
      You can also use add(), create(), or set() to create relationships, as long as you specify through_defaults for any required fields:

      >>> beatles.members.add(john, through_defaults={"date_joined": date(1960, 8, 1)})
      >>> beatles.members.create(
      ...     name="George Harrison", through_defaults={"date_joined": date(1960, 8, 1)}
      ... )
      >>> beatles.members.set(
      ...     [john, paul, ringo, george], through_defaults={"date_joined": date(1960, 8, 1)}
      ... )
    ```
  - We can use class Meta to define the constraint 













# AI rewrite 
# 📚 Django Quick Reference & Summary

This document collects and summarizes essential concepts, commands, and workflow steps for learning and developing with the Django web framework. It is structured to guide you from setup through deployment and touches on advanced topics.

---

## 🚀 Django Fundamentals

- **Project**: The main Django application containing settings and configurations; can host multiple apps.
- **App**: A modular component within a project, responsible for a distinct feature (e.g., polls, blog, user auth).

---

## 🔁 Django Request-Response Flow

1. **URLconf (`urls.py`)**: Maps URLs to view functions.
2. **Views (`views.py`)**: Handles incoming requests, executes logic, and returns responses (often rendering templates).
3. **Models (`models.py`)**: Defines your database structure and business data.
4. **Templates (`.html`)**: HTML files used for rendering web pages, including reusable `base.html`.

---

## 🛠️ Core Workflow Steps

### 1. Environment & Project Setup

- Create a virtual environment:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- Start a new Django project:
  ```bash
  django-admin startproject mysite .
  ```
- Run the development server:
  ```bash
  python manage.py runserver
  ```

### 2. App Creation & Model Management

- Create a new app:
  ```bash
  python manage.py startapp polls
  ```
- Define models in `models.py`.
- Create and apply migrations:
  ```bash
  python manage.py makemigrations polls
  python manage.py migrate
  ```
- Preview migration SQL:
  ```bash
  python manage.py sqlmigrate polls 0001
  ```
- Use the shell for querying:
  ```bash
  python manage.py shell
  ```
- Create an admin user:
  ```bash
  python manage.py createsuperuser
  ```

### 3. Views, URLs, and Templates

- Map URLs to views in `urls.py`.
- Write view functions in `views.py` to handle requests and render templates.
- Store HTML templates in the app's `templates` directory.

---

## 🔧 Advanced Topics

- **Forms**: Handle user input and validation, sending data to views.
- **Testing**: Use Django’s framework for automated testing of functionality.
- **Static Files**: Manage CSS, JS, and images for your project.
- **Admin Customization**: Use templates and configuration to personalize the admin site.
- **Third-party Packages**: Extend Django by installing and configuring reusable packages.
- **Reusable Apps**: Structure apps for sharing:
  - Python package with `__init__.py`
  - Include `README.md`, `LICENSE`, `pyproject.toml`, and manifest for non-Python files
  - Build with `python -m build`

---

## ☁️ Deployment Overview

- Prepare static files:
  ```bash
  python manage.py collectstatic
  ```
- Set up a production-ready server (e.g., using Gunicorn, Nginx).

---

## 📝 Learning Flow Summary

1. Set up a virtual environment.
2. Start a Django project.
3. Create apps for separate features.
4. Define models and run migrations.
5. Set up the admin site.
6. Write views and configure URLs.
7. Create templates for front-end.
8. Implement forms for user interaction.
9. Write automated tests.
10. Manage static files.
11. Deploy for production.

---

*This summary is meant as a quick reference for Django learning and development workflow.*









# Restful API 

  - Restful(REpresentational State Transfer)
  - Diango Rest Framework
