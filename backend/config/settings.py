from pathlib import Path
import os

# Chemin de base du projet (le dossier racine)
BASE_DIR = Path(__file__).resolve().parent.parent

# Clé secrète pour le projet Django (à garder privée en production)
SECRET_KEY = 'django-insecure-k_4m@1d2f3^-d5l!@lmvr0biaw92f2+&)mkqyj%^qa+h#%9^6&'

# Mode debug activé (à désactiver en production)
DEBUG = True

# Liste des hôtes autorisés (en local, vide suffit)
ALLOWED_HOSTS = []

# Applications installées, dont ta propre app 'portfolio'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',  # ton app portfolio
]

# Middleware: couches qui gèrent les requêtes et réponses
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # protection contre CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Fichier de configuration principal des urls
ROOT_URLCONF = 'config.urls'

# Configuration des templates (fichiers HTML dynamiques)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # tu peux ajouter ici un dossier de templates global
        'APP_DIRS': True,  # permet à Django de chercher dans chaque app
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',  # passe l'objet request aux templates
                'django.contrib.auth.context_processors.auth',  # info sur l'utilisateur connecté
                'django.contrib.messages.context_processors.messages',  # messages flash
            ],
        },
    },
]

# Application WSGI (interface entre serveur et Django)
WSGI_APPLICATION = 'config.wsgi.application'

# Base de données (SQLite par défaut, simple pour débuter)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validation des mots de passe (pour la sécurité)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Langue et fuseau horaire
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configuration des fichiers statiques (CSS, JS, images)
STATIC_URL = '/static/'  # URL pour accéder aux fichiers statiques

# Dossiers où Django va chercher les fichiers statiques en mode dev
STATICFILES_DIRS = [
     os.path.join(BASE_DIR, 'portfolio', 'static'),  # ton dossier static à la racine du projet
]

# Dossier où seront collectés les fichiers statiques lors du déploiement
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Type de champ primaire par défaut pour les modèles
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
