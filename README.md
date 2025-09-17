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

# Part 1

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

# Part 2 

$ python manage.py migrate
$ python manage.py makemigrations polls 
$ python manage.py sqlmigrate polls 0001
