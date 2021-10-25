# Namasys Assignment: Live at: https://user-login-123.herokuapp.com/
This App is related to how user can login from email and i make the Custom user, [AbstractUser](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project) in addition i add user authentication credentials only authorized user can access specific page.


## Local Setup
* Git clone: git clone https://github.com/vikash98k/namasys.git
* Go to Project directory: cd project
* Create A virtual environment: virtualenv venv(virtual environment name)
* requirement :  pip install -r requirements.txt
* Run migration commands: python manage.py makemigraion,python manage.py migrate
* Run locally: python manage.py runserver
