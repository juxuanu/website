
# Django settings for lutrisweb project.
import os
import socket

DEBUG = False
TEMPLATE_DEBUG = DEBUG
STATIC_SERVE = True

ADMINS = (
     ('Mathieu Comandon', 'strycore@gmail.com'),
)
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'lutris'             # Or path to database file if using sqlite3.
DATABASE_USER = 'lutris'             # Not used with sqlite3.
DATABASE_PASSWORD = 'lutrisweb'
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
language_code = 'en-us'

SITE_ID = 1
<<<<<<< TREE

# if you set this to false, django will make some optimizations so as not
=======
SERVER_NAME = "lutris.net"
# If you set this to False, Django will make some optimizations so as not
>>>>>>> MERGE-SOURCE
# to load the internationalization machinery.
USE_I18N = True

# absolute path to the directory that holds media.
# example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$%(3r)0s4ahdf(@a7l4d&f%@x^b3v_o&)m378l03q7y%ia4=w*'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'lutrisweb.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'registration',
    'lutrisweb.static',
    'lutrisweb.games',
    'lutrisweb.accounts',
)
ACCOUNT_ACTIVATION_DAYS = 3
LOGIN_REDIRECT_URL="/"
AUTH_PROFILE_MODULE = "accounts.Profile"

# Sending email

# Default email backend to use in production.
#EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# File based backend for development environment.
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = "/tmp/django-emails/"
DEFAULT_FROM_EMAIL = "admin@lutris.net"
EMAIL_SUBJECT_PREFIX = "[Lutris] "
