# core.settings.pŷ
# https://docs.djangoproject.com/en/3.2/topics/settings/
# https://docs.djangoproject.com/en/3.2/ref/settings/

from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-p=envkt!c6d!z(s*(0$@ksboik(erf&r4boqz63nek*6ut!$nh')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)
TEMPLATE_DEBUG = DEBUG
ADMIN_URL = 'tlb-admin'
META_KEYWORDS = ''
DEFAULT_CHARSET = 'UTF-8'
SITE_DESCRIPTION = ""
DEFAULT_CONTENT_TYPE = 'text/html'
SITE_NAME = 'ISLAM NEWS'

ALLOWED_HOSTS = []

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'blog.apps.BlogConfig'
]

PACKAGE_APPS = [
    'jet.dashboard',
    'jet',
    'ckeditor',
    'django.contrib.admin',
]

INSTALLED_APPS += LOCAL_APPS + PACKAGE_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'utils.function_utils.taleeb_context_processor',
            ],

            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True

# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True

# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'fr-fr'
USE_I18N = USE_L10N = USE_TZ = True
DATE_INPUT_FORMATS = ('%d/%m/%Y', '%Y-%m-%d')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

MEDIA_URL = '/media/'
STATIC_URL = '/static/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# staticfiles finders
# See: https://docs.djangoproject.com/en/3.1/ref/contrib/staticfiles/#staticfiles-finders

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Activez le backend de stockage WhiteNoise qui se charge de compresser
# les fichiers statiques et de créer des noms uniques pour chaque version
# afin qu'ils puissent être mis en cache à jamais en toute sécurité.

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# django/core/serializers/json.Serializer pour avoir la fonction de `dumps`.

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# Configuration django-jet
# https://jet.readthedocs.io/en/latest/config_file.html

JET_THEMES = [
    {
        'theme': 'default',
        'color': '#47bac1',
        'title': 'Default'
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

JET_SIDE_MENU_COMPACT = True
JET_CHANGE_FORM_SIBLING_LINKS = True

# https://pypi.org/project/django-ckeditor/

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar_Custom': [
            {
                'name': 'document',
                'items': [
                    'Source', '-', 'Save', 'NewPage', 'Preview',
                    'Print', '-', 'Templates'
                ]
            },
            {
                'name': 'clipboard',
                'items': [
                    'Cut', 'Copy', 'Paste', 'PasteText',
                    'PasteFromWord', '-', 'Undo', 'Redo'
                ]
            },
            {
                'name': 'editing',
                'items': ['Find', 'Replace', '-', 'SelectAll']},
            {
                'name': 'forms',
                'items': [
                    'Form', 'Checkbox', 'Radio', 'TextField', 'Textarea',
                    'Select', 'Button', 'ImageButton', 'HiddenField'
                ]
            },
            '/',
            {
                'name': 'basicstyles',
                'items': [
                    'Bold', 'Italic', 'Underline', 'Strike', 'Subscript',
                    'Superscript', '-', 'RemoveFormat'
                ]
            },
            {
                'name': 'paragraph',
                'items': [
                    'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
                    'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter',
                    'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language'
                ]
            },
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {
                'name': 'insert',
                'items': [
                    'Image', 'Youtube', 'Flash', 'Table', 'HorizontalRule', 'Smiley',
                    'SpecialChar', 'PageBreak', 'Iframe'
                ]
            },
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['CodeSnippet']},
            {'name': 'about', 'items': ['About']},
            '/',
            {'name': 'yourcustomtools', 'items': [
                'Preview',
                'Maximize',
            ]},
        ],
        'toolbar': 'Custom',
        'toolbarGroups': [{'name': 'document', 'groups': ['mode', 'document', 'doctools']}],
        'height': 400,
        'filebrowserWindowHeight': 725,
        'filebrowserWindowWidth': 940,
        'toolbarCanCollapse': True,
        'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
            'codesnippet',
        ]),
    }
}

# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console", "mail_admins"],
            "propagate": True,
        },
    },
}
