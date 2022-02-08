# Django Chat Application
a simple chat built with Django, Django-Channels and Redis.

## Used in this app:
- python3
- django
- Redis
- django-channels
- bootstrap
- sqlite3 database

## Run this app:
1. clone or download the project.
2. change directory to ``` chat-app-django```
3. make sure you have ``python3``, ```pip``` and ```virtualenv``` installed in your machine.
4. create virtualenv: ```python3 -m venv venv```
5. active virtualenv: mac & linux os: ```source venv/bin/activate```, windows os: ```venv\scripts\activate```
6. install app requirements: ```pip install -r requirements.txt```
7. databse migrate: ```python manage.py migrate```
8. run the server: ```python manage.py runserver```
9. you should be able to open this address now: http://127.0.0.1:8000/

## To-Do:
- [ ] implement one-to-one private chat
- [ ] show users profile, photo, username and chat btn
- [ ] display user public-information
- [ ] edit profile
