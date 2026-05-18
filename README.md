from django.http import HttpResponse

# WEB DEVELOPMENT COUPLE

## Hello! It's a project for WEB DEVELOPMENT COUPLE.

Just a project for education

## Laboratory work 1 (02.11.2026)
<details>
<summary>CLICK HERE TO SEE THE TASK CONDITION</summary>

> ### Задача
> Вам подвернулся подходящий случай применить полученные знания на практике. 
> Известная медицинская фирма Unicorn разработала новый монитор сердечного 
> ритма heart tracker, и вас пригласили написать программный модуль для этого устройства. 
> Заказчик составил техническое задание, которому вы должны следовать для успешного 
> выполнения проекта. Вам предстоит написать константы и функции.

> ### **Техническое задание**
> Программный модуль для обработки данных монитора сердечного ритма 
> heart tracker фирмы Unicorn.

> ### **Входные данные**
> Модуль получает от микросхемы-контроллера пакеты данных в виде кортежей.
> Пакеты передаются в программу в момент обращения к трекеру (при нажатии на кнопку). 
> Порядок значений в пакете данных:
> _**(<time>, <heart_rate>)**_
>- <time>: время создания пакета; значение типа str; формат:
>'часы:минуты:секунды'.
>- <heart_rate>: частота сердечных сокращений, измеренная пользователем 
> с момента последнего обращения; значение типа int.

> При передаче пакетов могут случаться сбои, это надо учесть в программе.
> При поступлении пакета нужно проверить его; передавать пакет на обработку можно только
> после проверки.

> ### **Возможные ошибки при получении пакетов:**
> 1. Пакет меньшей или большей длины.
> 2. У одного или нескольких параметров в пакете пустое значение.
> 3. Значение времени в переданном пакете меньше или равно предыдущему записанному значению 
> (время считается в рамках одних суток).

> ### **Результат выполнения программы**
> 1. Полученные пакеты должны сохраняться в словаре storage_data. 
> Ключами для него будут значения времени, а значениями — частота сердечных сокращений.
> 2. В терминал должно выводиться сообщение, например такое (в начале и в конце сообщения должна выводиться пустая строка):
     ```
     _Время_: 09:36:02.
     _Частота сердечных сокращений за сегодня_: 72 уд/мин.
     'Хороший результат, Вы движетесь в правильном направлении!'
     ```
> 3. Также должно выводиться мотивирующее сообщение. Его содержание должно зависеть от интенсивности сердечного ритма:
    > ```
    >     - 100 уд/мин и более: 'Осторожно что-то не так! Обратитесь к врачу.'
    >     
    >     - 80 уд/мин и более: 'Осторожно успокойтесь!'
    >     
    >     - 60 уд/мин и более: 'Хороший результат, Вы движетесь в правильном направлении!'
    > 
    >     - Менее 60 уд/мин: 'Главное — быть активным!'
    > ```
> 4. Программа должна возвращать словарь storage_data, чтобы можно было продолжить обработку данных в других программах.

> ### **Точка входа в программу**
> - Функция обработки пакетов _accept_package()_ — это точка входа в программу, функция, которая вызывается первой. На вход она принимает пакет с данными. 
> - Функция _accept_package()_ должна вернуть словарь storage_data, в который добавлены данные из полученного пакета. Из этой функции по цепочке вызываются другие функции, каждая из которых отвечает за свою часть работы. 
> - Сразу после старта должна выполниться функция _check_correct_data()_, проверяющая корректность полученного пакета. Она может вернуть true или False, что повлияет на дальнейшее выполнение базовой функции.

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

### 4. Create model
In app/models.py
```python 
class HeartRateRecord(models.Model):
    time = models.CharField(max_length=8, unique=True, verbose_name='Время записи')
    heart_rate = models.CharField(verbose_name='Частота сердечных сокращений')

    def __str__(self):
        return f'{self.time} -> {self.heart_rate} уд/мин.'
```
After the changes in app/models.py u have to create migrations for data updates
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create functions for interaction with database
In app/view.py
```python

# data display
def accept_package(request):
    time = request.GET.get('time')
    heart_rate = request.GET.get('rate')

    try: heart_rate = int(heart_rate)
    except(ValueError, TypeError):
        return HttpResponse(
            'Error: Incorrect heart rate recording format',
            status=400)

    if not check_correct_data(time, heart_rate):
        return HttpResponse(
            'Error: Validation or time failure',
            status=400)

    HeartRateRecord.objects.create(time=time, heart_rate=heart_rate)
    message = get_motivation_message(heart_rate)

    response_html = f"""
<div>
    <div>Время: {time}</div>
    <div>Частота сердечных сокращений: {heart_rate} уд/мин.</div>
    <div>'{message}'</div>
</div>
"""
    return HttpResponse(response_html)


# data validation 
def check_correct_data(time: str, rate: int) -> bool:
    if not time or rate is None:
        return False

    elif not (30 <= rate <= 250): # для разумных пределов
        return False
    else:
        last_val = HeartRateRecord.objects.order_by('time').last()
        if last_val and last_val.time >= time :
            return False
        return True

# message display 
def get_motivation_message(heart_rate: int) -> str:
    if heart_rate >= 100:
        return 'Осторожно что-то не так! Обратитесь к врачу.'
    elif 80 <= heart_rate < 100:
        return 'Осторожно успокойтесь!'
    elif 60 <= heart_rate < 80:
        return 'Хороший результат, Вы движетесь в правильном направлении!'
    else:
        return 'Главное — быть активным!'
```

### 6. URL Settings
In app create urls.py:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('track/', views.accept_package, name='accept_package'),
]
```
And in mysite/urls.py:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]
```
### 7. Testing
If u run server at http://127.0.0.1:8000/
```bash
python manage.py runserver
```
u can see
![img_1.png](img/img_1.png)

If u go to http://127.0.0.1:8000/track/
U can see message "Error: Incorrect heart rate recording format"
![img_2.png](img/img_2.png)

For testing you can add the time and heart rate: 
http://127.0.0.1:8000/track/?time=09:08:50&rate=80

![img_3.png](img/img_3.png)

http://127.0.0.1:8000/track/?time=09:80:02&rate=72

![img_4.png](img/img_4.png)

But after page updating:

![img_5.png](img/img_5.png)

### Saved at the commit "laboratory work 1 (02.11.2026)"

## Laboratory work 2 (02.18.2026)

<details>
    <summary>CLICK HERE TO SEE THE TASK CONDITION</summary>

> **Задание для самостоятельной работы:** Разработка веб-приложения на
> Django для медицинской клиники "Здоровье+"


> **Цель задания:**
> Закрепить знания о создании и настройке веб-приложений на Django, а также
> научиться работать с моделями, представлениями и маршрутизацией.
>
> **Задание:**
> Создайте веб-приложение для медицинской клиники "Здоровье+",

> **Функции**
> 1. Создание проекта и приложения appointments
> 2. Представлени:
>   В файле views.py создайте следующие функции заглушки:
```python
from django.http import HttpResponse

def appointment_list(request):
""" Отображает список всех записей на прием. """
# Заглушка: Возвращаем текстовое сообщение
    return HttpResponse("Список всех записей на прием.")

def appointment_detail(request, appointment_id):
""" Отображает детали конкретной записи на прием. """
# Заглушка: Возвращаем текстовое сообщение с ID записи
    return HttpResponse(f"Детали записи на прием с ID: {appointment_id}.")

def create_appointment(request):
""" Форма для создания новой записи на прием. """
# Заглушка: Возвращаем текстовое сообщение
    return HttpResponse("Форма для создания новой записи на прием.")
``` 
> 3. Маршруты:
> - В файле urls.py приложения appointments настройте маршруты
для ваших представлений:
>   - Главная страница (например, /): отображает приветственное
сообщение.
>   - /appointments/: отображает список записей на прием.
>   - /appointments/<int:pk>/: отображает детали конкретной
записи.
>   - /appointments/create/: форма для создания новой записи.

</details>

### 1. Create application "appointments"

```bash
django-admin startapp appointments
```
### 2. Create features appointment_list, appointment_detail, create_appointment
In appointments/view.py
```python
def home(request):
    return HttpResponse('HELLO WORLD')
def appointment_list(request):
    return HttpResponse('List of all appointments')

def appointment_detail(request, appointment_id):
    return HttpResponse(f'Appointment details with ID: {appointment_id}')

def create_appointment(request):
    return HttpResponse('Appointment form')
```
### 3. URL settings
Create rotes in application (in appointments/urls.py):
```python
urlpatterns = [
    path('', views.home, name='home'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/create/', views.create_appointment, name='create_appointments'),
    path('appointments/<int:appointment_id>', views.appointment_detail, name='appointment_detail')
]
```
Connecting rotes in mysite/urls.py:
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appointments.urls'))
]
```
### 4. Testing
When we start the server in http://127.0.0.1:8000/ :

![img_6.png](img/img_6.png)

But at the http://127.0.0.1:8000/appointments :

![img_7.png](img/img_7.png)

At the http://127.0.0.1:8000/appointments/8 (for example):

![img_8.png](img/img_8.png)

At the http://127.0.0.1:8000/appointments/create :

![img_9.png](img/img_9.png)

### Saved at the commit "laboratory work 2 (02.18.2026)"