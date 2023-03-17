# This is a minimal Django Project for tests

SECRET_KEY = '7h3_$3cr37'

DEBUG = True

INSTALLED_APPS = [
    'dj_ec_idcardfield',
    'tests.sample_app',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

ROOT_URLCONF = __name__

urlpatterns = []
