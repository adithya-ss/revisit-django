# revisit-django
Revisiting and covering topics/concepts of Django Web Framework

Installing a vitual environment:
    - pip install virtualenv

Creating and activating a virtual environment:
    - python -m venv <virtual_env_name>
    - source /<virtual_env_name>/Scripts/activate

Installing django inside virtual environment:
    - python -m pip install Django

Creating a project:
    - django-admin startproject <project_name>
    - A new folder is auto-generated.

Creating a django app:
    - python manage.py startapp <app_name>
    - A new folder is auto-generated.
    - Apps can be packed and imported in another django project, if the functionality remains common.
    - Automated tests can be written inside the tests.py inside app folder.

Start the django server:
    - python manage.py makemigrations **If the execution is stuck at "Watching for file changes with StatReloader"
    - python manage.py migrate **If the execution is stuck at "Watching for file changes with StatReloader"
    - python manage.py runserver