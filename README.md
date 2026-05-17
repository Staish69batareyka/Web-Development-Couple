# WEB DEVELOPMENT COUPLE

## Hello! It's a project for WEB DEVELOPMENT COUPLE.

Just a project for education

## Laboratory work 1 (02.11.2026)
<details>
<summary>Нажмите, чтобы открыть</summary>

> Это текст цитаты, который будет скрыт.
> Внутри цитаты можно использовать любые форматирования, например **жирный шрифт**.

</details>


### 1. How to create Django project

```bash
# create virtual environment called venv
python -m venv venv 

# activate virtual environment in Windows
venv\Scripts\activate 

# install django
pip install django

# create django project
django-admin start project mysite . 
# The dot indicates to create files only in the specified folder, so as not to create new ones

# create django app 
python manage.py startapp app
```
**File structure**

- _**manage.py**_ - main file for project control
- _**mysite/**_ - project settings
- _**app/**_ - application

### 2. Project registration
In mysite/settings.py
```python 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # add application
    'app'
]
```
### 3. Start the server
If you run
```bash
python manage.py runserver
```
and navigate to the path in the terminal
(for example 'Starting development server at http://127.0.0.1:8000/')

U can see a page like this in your browser:
![img.png](img/img.png)