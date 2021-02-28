## django-admin startproject mysite
## python manage.py startapp home
## python manage.py runserver
## python manage.py makemigrations
## pthon manage.py migrate
## python manage.py createsuperuser


### Django administration text
- admin.site.site_header = "UMSRA Admin"
- admin.site.site_title = "UMSRA Admin Portal"
- admin.site.index_title = "Welcome to UMSRA Researcher Portal"

### Django Database Settings
- Register your models in admin.py
- admin.site.register(Contact)
- 
- code  'home.apps.HomeConfig',   this in settings.py at Installed apps