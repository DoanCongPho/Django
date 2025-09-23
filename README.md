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
