"""
Django settings for MainTechforing project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from decouple import config
import os
import environ

env = environ.Env()
environ.Env.read_env()
PAYPAL_USER = env('paypal_user')
PAYPAL_PASS = env('paypal_pass')
PAYPAL_URL = env('paypal_url')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR.joinpath('templates')
STATIC_DIR = BASE_DIR.joinpath('static')
MEDIA_DIR = BASE_DIR.joinpath('media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j55@su5sxajtqf_yed#+^vn&p0l=ovow1^6cp$&05so^8^l3th'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['0.0.0.0', '44.242.38.198', 'main.techforing.com', 'pcs.techforing.com', 'training.techforing.com',
                 '127.0.0.1', 'localhost', '.techforing.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Installed Apps
    'Academy',
    'Account',
    'BusinessSecurity',
    'PersonalSecurity',
    'Blog',
    'Api',

    # django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # tinymce
    'tinymce',

    # djangorestframework
    'rest_framework',

    # django-phonenumber-field
    'phonenumber_field',

    # django-crispy-forms
    'crispy_forms',

    # django-countries, pyuca
    'django_countries',

    # django-cleanup
    'django_cleanup.apps.CleanupConfig',

    # django_hosts
    'django_hosts',

    # Cors
    'corsheaders',

    # Timezone
    'timezone_field',

    # CronTab
    'django_crontab',
]

# CSRF_TRUSTED_ORIGINS = ['https://*.techforing.com', 'https://techforing.com', 'http://127.0.0.1:8000']

# Django-Rest-Framework Settings
REST_FRAMEWORK = {
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    # ),
    # 'DEFAULT_PARSER_CLASSES': [
    #     'rest_framework.parsers.JSONParser',
    # ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}

# tinymce Settings
TINYMCE_DEFAULT_CONFIG = {
    "theme": "silver",
    "height": 500,
    "menubar": 'file edit view insert format tools table help',
    "plugins": 'print, preview, importcss, searchreplace, autolink, autosave, '
               'save, directionality, visualblocks, visualchars, fullscreen, image, link, media, '
               'template, codesample, table, charmap, hr, pagebreak, nonbreaking, anchor, toc, insertdatetime, '
               'advlist, lists, wordcount, textpattern, noneditable, '
               'help, charmap, quickbars, emoticons, '
               'searchreplace,visualblocks,code,fullscreen,media,table,paste, code,help,wordcount',
    "toolbar1": "undo redo toc | fontselect fontsizeselect formatselect lineheight | bold italic underline "
                "strikethrough superscript subscript | forecolor backcolor "
                "removeformat | alignleft "
                "aligncenter alignright alignjustify |  numlist bullist | outdent indent |  searchreplace hr "
                "charmap emoticons table pagebreak |  insertdatetime image insertfile media template link anchor "
                "codesample | "
                "ltr rtl |fullscreen preview print | help",
    'file_browser_callback': 'filebrowser'

}
TINYMCE_SPELLCHECKER = True
TINYMCE_FILEBROWSER = True


# Crispy_Forms_Settings
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# allauth Settings
# Provider specific settings
# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         # For each OAuth based provider, either add a ``SocialApp``
#         # (``socialaccount`` app) containing the required client
#         # credentials, or list them here:
#         'APP': {
#             'client_id': '123',
#             'secret': '456',
#             'key': ''
#         }
#     }
# }
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN = 180
# ACCOUNT_LOGIN_ON_PASSWORD_RESET = True

ACCOUNT_FORMS = {
    'login': 'Account.forms.LoginForm2',
    'signup': 'Account.forms.RegistrationForm',
    # 'login': 'allauth.account.forms.LoginForm',
    # 'signup': 'allauth.account.forms.SignupForm',
    # 'add_email': 'allauth.account.forms.AddEmailForm',
    # 'change_password': 'allauth.account.forms.ChangePasswordForm',
    # 'set_password': 'allauth.account.forms.SetPasswordForm',
    # 'reset_password': 'allauth.account.forms.ResetPasswordForm',
    # 'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
    # 'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
}

SITE_ID = 1
LOGIN_REDIRECT_URL = '/account/profile/'
# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')
DEFAULT_FROM_EMAIL = 'Techforing <testtechforing@gmail.com>'

MIDDLEWARE = [
    'django_hosts.middleware.HostsRequestMiddleware',  # for django-host
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_hosts.middleware.HostsResponseMiddleware',  # for django-host
]

X_FRAME_OPTIONS = 'SAMEORIGIN'

# For Development
# SESSION_COOKIE_DOMAIN = '127.0.0.1'
# SESSION_COOKIE_NAME = 'techforingsessionid'
# SESSION_COOKIE_SECURE = True
# SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
# ROOT_URLCONF = 'MainTechforing.urls'
# ROOT_HOSTCONF = 'MainTechforing.hosts'
# DEFAULT_HOST = 'main'
# PARENT_HOST = '127.0.0.1:8000'

# For Production
SESSION_COOKIE_DOMAIN = '.techforing.com'
SESSION_COOKIE_NAME = 'techforingsessionid'
SESSION_COOKIE_SECURE = True
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
ROOT_URLCONF = 'MainTechforing.urls'
ROOT_HOSTCONF = 'MainTechforing.hosts'
DEFAULT_HOST = 'main'
PARENT_HOST = 'techforing.com'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': ['templates'],
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Blog.context_processor.BlogSubscribe',
                'BusinessSecurity.context_processor.NotificationCount',
            ],
        },
    },
]

WSGI_APPLICATION = 'MainTechforing.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# For Development
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# For Production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': 'root',
        'PASSWORD': env('DB_PASSWORD'),
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'
# STATICFILES_DIRS = ['static']
STATICFILES_DIRS = [BASE_DIR / 'static']

# tiny config
TINYMCE_JS_URL = os.path.join(STATIC_URL, "tinymce/tinymce.min.js")
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, "tinymce")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Cors Settings
# CORS_ALLOWED_ORIGINS = [
#     "https://techforing.com",
#     "https://www.techforing.com",
#     "https://main.techforing.com",
#     "https://bcs.techforing.com",
#     "https://pcs.techforing.com",
#     "https://academy.techforing.com",
#     "https://training.techforing.com",
#     "http://localhost:8080",
#     "http://127.0.0.1:8000",
#     "http://44.242.38.198",
#     "http://0.0.0.0",
# ]
CORS_ALLOW_ALL_ORIGINS = True
SECURE_REFERRER_POLICY = "strict-origin"

# CORS_ORIGIN_WHITELIST = [
#     "https://techforing.com",
#     "https://www.techforing.com",
#     "https://main.techforing.com",
#     "https://bcs.techforing.com",
#     "https://pcs.techforing.com",
#     "https://academy.techforing.com",
#     "https://training.techforing.com",
#     "http://localhost:8080",
#     "http://127.0.0.1:8000",
#     "http://44.242.38.198",
#     "http://0.0.0.0",
# ]
#
CSRF_TRUSTED_ORIGINS = [
    "https://techforing.com",
    "https://www.techforing.com",
    "https://main.techforing.com",
    "https://bcs.techforing.com",
    "https://pcs.techforing.com/",
    "https://academy.techforing.com",
    "https://training.techforing.com",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "http://44.242.38.198",
    "http://0.0.0.0",
]
CSRF_COOKIE_DOMAIN = '.techforing.com'

CORS_URLS_REGEX = r'^/api/.*$'
CORS_ALLOW_CREDENTIALS = True
SESSION_COOKIE_SAMESITE = 'None'

# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'

# Login
LOGIN_URL = '/accounts/login/'
AUTH_USER_MODEL = 'Account.User'

# CronJob Settings
CRONJOBS = [
    ('0 0 * * *', 'BusinessSecurity.cronjob.PaypalSubscriptionCheck')
]