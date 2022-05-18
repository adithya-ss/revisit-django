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

Model Migrations:
    - python manage.py makemigratons
    - python manage.py migrate

<!-- PROJECT NOTES -->

Templates: 
- Pre-define HTML files which can be enriched by dynamic data.
- Sub folders are created for defining/creating template files for a specific app.

Static content: 
- Something which is not influenced by the python code.
- Created inside a sub folder, specific for app.

Django Templating:
    - {% static 'meetups/styles/base.css' %} - Specify the static resource to be loaded on the page.
    - {% load static %} - Command to load the static file.
    - Interpolation syntax can be used anywhere within the html code. Tags and also other places. No restrictions.

Django Models:
    - Class representation of data to be stored in the database.
    - Base class inheritance from Model

Administration
    - While trying to create a super user using 'python manage.py createsuperuser' on a windows machine, we have to prefix
    the command by winpty. This is to avoid "Superuser creation skipped due to not running in a TTY" error.

Media/Images:
    - A new package called "Pillow" has to be installed, which will be used by django under the hood, to work with images.
    - The images need not only be uploaded, it also has to be served. Images are served through the projects's urls.py
    - The images are static resources/files.