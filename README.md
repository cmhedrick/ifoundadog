# iFoundADog

### Requirements:
1. Python 3.6+
2. Git
3. Virtualenv (Recommended)

### Installation UNIX:
1. clone the project
	```bash
	git clone https://github.com/cmhedrick/ifoundadog.git
	```
2. navigate to the `ifoundadog` directory 
	```bash
	cd ifoundadog
	```
3. create a virtual environment with python3
	```bash
	virtualenv -p python3 env
	```
4. activate the virtual environment
	```bash
	source env/bin/activate
	```
5. use pip to install the needed dependencies into your virtual environment
	```bash
	pip install -r requirements.txt
	```
6. navigate to the `site_ifoundadog` directory
	```bash
	cd site_ifoundadog/
	```
7. create a copy of the `settings_config.py.example` and name it settings_config.py
	```bash
	cp settings_config.py.example settings_config.py
	```
8. open the `settings_config.py` file and edit the SECRET_KEY with one generated from the site provided in the source comment.
9. navigate to the `app_ifoundadog` directory
	```bash
	cd ../app_ifoundadog
	```
10. make a copy of the `config-example.py` and name the copy `config.py`
	```bash
	cp config-example.py config.py
	```
11. open the `config.py` file and edit the API_KEY, make it to the one you generate from the url mentioned in the source.
12. navigate back into the main directory
	```bash
	cd ..
	```
13. run the migrate command from the `manage.py` file to apply migrations to the database
	```bash
	python manage.py migrate
	```
14. create a superuser for the application for the initial login
	```bash
	python manage.py createsuperuser
	```
15. run the local server
	```bash
	python manage.py runserver
	```
16. in your browser go to `0.0.0.0:8000/admin/` and attempt to login

17. Explore the rest of the site by going back to the initial screen at `0.0.0.0:8000/`

### OS X certification store issue
When running the app in OS X, and looking up dogs by license, you may run into errors related to validating the SSL certificate.
The urllib library of Python 3.6 depends on a different cert store than OS X's default. More information can be found in the readme.rtf file accompanying the installation. **The fix** is to obtain the Python-specific store by running:
/Applications/Python 3.6/Install Certificates.command
SSL certificate verification should then function as expected. 


### Installation Windows:
1. clone the project
    ```bash
    git clone https://github.com/cmhedrick/ifoundadog.git
    ```
2. navigate to the ifoundadog directory
    ```bash
    cd ifoundadog
    ```
3. create a virtual environment, once created you'll be in the virtual environment already. This can be observed when you see "(env)" at the beginning of the command prompt.
    ```bash
    mkvirtualenv env
    ```
4. bind the virtual environment to the `ifoundadog` directory    
    ```bash
    setprojectdir .
    ```
5. next install the python module dependencies using pip
    ```bash
    pip install -r requirements.txt
    ```
6. navigate to the `site_ifoundadog` directory
    ```bash
    cd site_ifoundadog/
    ```
7. create a copy of the `settings_config.py.example` and name it `settings_config.py`
    ```bash
    cp settings_config.py.example settings_config.py
    ```
8. open the `settings_config.py` file and edit the SECRET_KEY with one generated from the site provided in the source comment.
9. navigate to the `app_ifoundadog` directory
    ```bash
    cd ../app_ifoundadog
    ```
10. make a copy of the `config-example.py` and name the copy `config.py`
    ```bash
    cp config-example.py config.py
    ```
11. open the `config.py` file and edit the API_KEY, make it to the one you generate from the url mentioned in the source.
12. change back into the main directory
    ```bash
    cd ..
    ```
13. run the migrate command from the `manage.py` file to apply migrations to the database
    ```bash
    python manage.py migrate
    ```
14. create a superuser for the application for the initial login
    ```bash
    python manage.py createsuperuser
    ```
15. run the local server
    ```bash
    python manage.py runserver
    ```
16. in your browser go to `http://127.0.0.1:8000/admin/` and attempt to login
17. explore the rest of the site by going back to the initial screen at `http://127.0.0.1:8000/`