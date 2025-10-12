# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'feedback',
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
        'USER' : 'root',
        'PASSWORD' : '',
    }
}

INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]