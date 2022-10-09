# PizzaMama
Django commands

- Install Django : Pip install django 
- Create new project : django-admin startproject <projectName>

- Start web server  : 
    - 1.  Go to server folder where manage.py file is present 
    - 2.  Start server : python3 mange.py runserver 

- Create application : 
    - 1. Go to mange.py server 
    - 2. Create new application : python3 manage.py start app <myApp>

- Perform migrations on models: 
    - 1. Go to app folder > Go to apps file > Get class name
    - 2. Map path App > apps > ClassName into setting.py
    - Command to create migrations for models : python3 manage.py makemigrations => Generate migrations files under migrations folder 
    - Apply migrations to database : python3 manage.py migrate

- Create superuser : 
    - Python3 manage.py createsuperuser


- Add application to admin interface :

			from .models import <ClassModel>
			admin.site.register(<ClassModel>)


- Pseudo python code in html page :

            <ul>
                {% for pizza in pizzas %}
                    <li>{{ pizza.name }}</li>
                  {% endfor %}
            </ul>

- Changes to do at every production deployment :
  1. python manage.py migrate (If changes on db structure)
  2. python manage.py loadstatic (to update images and css)
	
