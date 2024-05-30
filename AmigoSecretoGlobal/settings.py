from pathlib import Path
from dotenv  import load_dotenv
from os      import environ
from urllib  import parse
load_dotenv()

BASE_DIR        = Path(__file__).resolve().parent.parent
SECRET_KEY      = environ.get('SECRET_KEY')
DEBUG           = True
ALLOWED_HOSTS   = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'AmigoSecreto'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AmigoSecretoGlobal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'AmigoSecreto' / 'Views'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'AmigoSecretoGlobal.wsgi.application'

parse.uses_netloc.append('postgres')
url = parse.urlparse(environ.get('DATABASE_URL'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': url.hostname,
        'PORT': url.port,
        'USER': url.username,
        'PASSWORD': url.password,
        'NAME': url.username
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE   = 'pt-br'
TIME_ZONE       = 'America/Sao_Paulo'

USE_I18N    = True
USE_TZ      = True

STATIC_URL  = 'static/'
STATIC_ROOT = BASE_DIR / 'AmigoSecreto' / 'Static'
MEDIA_URL   = 'media/'
MEDIA_ROOT  = BASE_DIR / 'AmigoSecreto' / 'Media'

EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS       = True
EMAIL_USE_SSL       = False
EMAIL_HOST          = environ.get('EMAIL_PROVIDER')
EMAIL_HOST_USER     = environ.get('EMAIL')
EMAIL_HOST_PASSWORD = environ.get('EMAIL_PASSWORD')
EMAIL_PORT          = 587
DEFAULT_FROM_EMAIL  = 'HenriTech Amigo Secreto <' + environ.get('EMAIL') + '>'

LOGIN_URL           = 'login/'
LOGIN_REDIRECT_URL  = 'app/'
LOGOUT_URL          = 'logout/'
LOGOUT_REDIRECT_URL = 'login/'

SESSION_ENGINE      = 'django.contrib.sessions.backends.db'

DEFAULT_AUTO_FIELD  = 'django.db.models.BigAutoField'
