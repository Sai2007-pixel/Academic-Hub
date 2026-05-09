import cloudinary
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-1234567890'

DEBUG = False

ALLOWED_HOSTS = ['*']


# ✅ INSTALLED APPS
INSTALLED_APPS = [

    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'cloudinary_storage',
    'cloudinary',

    'hub',
]


# ✅ MIDDLEWARE
MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]


ROOT_URLCONF = 'academichub.urls'


# ✅ TEMPLATES (ADD DIRS FOR GLOBAL TEMPLATES)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # 👈 important improvement
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'academichub.wsgi.application'


# ✅ DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ✅ PASSWORD VALIDATION
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


# ✅ LANGUAGE & TIME
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True



STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# # ✅ STATIC FILES
# STATIC_URL = 'static/'
# STATICFILES_DIRS = [BASE_DIR / 'staticfiles']   # 👈 optional but useful


# ✅ DEFAULT FIELD
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'thedigitalhub16@gmail.com'

EMAIL_HOST_PASSWORD = 'yiyyjenuitnyxyhw'

JAZZMIN_SETTINGS = {

    "site_title": "Academic Hub Admin",

    "site_header": "Academic Hub Administration",

    "site_brand": "Academic Hub",

    "welcome_sign": "Welcome to Academic Hub Backend",

    "copyright": "Sai Chandra",

    "show_sidebar": True,

    "navigation_expanded": True,

    "icons": {

        "hub.Branch": "fas fa-layer-group",

        "hub.Semester": "fas fa-calendar",

        "hub.Subject": "fas fa-book",

        "hub.File": "fas fa-file-pdf",

        "hub.FileCategory": "fas fa-folder"

    },

}


cloudinary.config(
    cloud_name='dxqv9zh4t',
    api_key='441433973451126',
    api_secret='g1oFPA-lVJPwlA3Nl_tVaFSgGXo',
)

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}