"Python django portfolio werbsite " 



1. Download python and install.
2. In cmd  put "pip install  django".
3. In cmd  put "pip install  virtualenvwrapper-win".
4. In cmd put "mkvirtualenv <Virtual-env-name> ". #after this we will enter in virtual environment.
5. Now we will install django in virtual env with put in cmd " pip install django".
6. Now by going to specific directoty where we want tocreate django project  we put " django-admin startproject <project-Name>.

--we can deactivate virtual env by typing "deactivate".
-- We can go back to virtual env using "workon <app-name>.

7. Each project can have many app we can crwate another app by using in root directory.   "python manage.py startapp myproject"

8. Run django project:     "python manage.py runserver"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myproject',
        'USER':'postgres',
        'PASSWORD':';/.,m',
        'HOST':'localhost'
    }
}

ALLOWED_HOSTS = [
    '34.201.22.224:8000'
]
