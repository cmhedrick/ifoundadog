# iFoundADog

### Requirements:
1. Python 3.6+
2. Git
3. Virtualenv (Recommended)

### Installation UNIX:
1. clone the project
`git clone https://github.com/cmhedrick/ifoundadog.git`
2. change into the ifoundadog directory.
`cd ifoundadog`
3. create a virtual environment with python3
`virtualenv -p python3 env`
4. activate the virtual environment
`source env/bin/activate`
5. use pip to install the needed dependencies into your virtual environment
`pip install -r requirements.txt`
6. change into the site_ifoundadog directory
`cd site_ifoundadog/`
7. create a copy of the settings_config.py.example and name it settings_config.py
`cp settings_config.py.example settings_config.py`
8. open the settings_config.py file and edit the SECRET_KEY with one generated from the site provided in the source comment.
9. change into the app_ifoundadog directory
`cd ../app_ifoundadog`
10. make a copy of the config-example.py and name the copy config.py
`cp config-example.py config.py`
11. open the config.py file and edit the API_KEY, make it to the one you generate from the url mentioned in the source.
12. change back into the main directory
`cd ..`
13. run the migrate command from the manage.py file to apply migrations to the database
`python manage.py migrate`
14. create a superuser for the application for the initial login
`python manage.py createsuperuser`
15. run the local server
`python manage.py runserver`
16. in your browser go to 0.0.0.0:8000/admin/ and attempt to login
17. Explore the rest of the site by going back to the initial screen at 0.0.0.0:8000/