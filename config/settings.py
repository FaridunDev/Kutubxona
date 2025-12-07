import os
from pathlib import Path
from datetime import timedelta
BASE_DIR = Path(__file__).resolve().parent.parent

# ===============================
# 1. XAVFSIZLIK (SECURITY)
# ===============================
try:
    SECRET_KEY = os.environ['SECRET_KEY']
except KeyError:
    if os.environ.get('DJANGO_DEBUG', 'True') == 'True':
        SECRET_KEY = 'django-insecure-36-(4k6or1b=rn+o5b7r$^81dhz3omo-&uh9tkvwhi^dw%15go' 
    else:
        raise Exception("SECRET_KEY muhit o'zgaruvchisi topilmadi!")


DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True' 
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',') 
# ===============================
# 2. Ilovalar (INSTALLED APPS)
# ===============================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Uchinchi tomon ilovalari (API va autentifikatsiya uchun)
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist', 
    'django_filters', 
    'drf_yasg', 
    'corsheaders', 
    
    # Lokal loyiha ilovalari
    'accounts',
    'books',
    'borrowing',
    'inventory',
    'reviews',
    'suppliers',
    'moderation',
    'logs',
]

# ===============================
# 3. Middleware
# ===============================

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', 
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'
AUTH_USER_MODEL = "accounts.User" # Maxsus User modelini belgilash
# ===============================
# 4. Ma'lumotlar BAZASI (PostgreSQL)
# ===============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # Ma'lumotlar DB nomini .env dan olish
        'NAME': os.environ.get('DB_NAME', 'Kutubxona'),
        # Ma'lumotlar DB foydalanuvchisini .env dan olish
        'USER': os.environ.get('DB_USER', 'postgres'), 
        # --- PAROLNI YASHIRISH ---
        'PASSWORD': os.environ.get('DB_PASSWORD', 'admin123'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}


#Qolgan qismlar (Password validation, Internationalization, Static files, DEFAULT_AUTO_FIELD)

# ===============================
# 5. REST Framework + JWT Sozlamalari
# ===============================

REST_FRAMEWORK = {
    # Hamma API so'rovlari uchun default autentifikatsiya usuli
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # Agar ruxsatnoma view ichida belgilangan bo'lmasa, default ruxsatnoma.
    # Productionda bu IsAuthenticated bo'lishi kerak.
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    # Filtrlash mexanizmi
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

SIMPLE_JWT = {
    # Access Token muddati (Hozirgi: 60 daqiqa)
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60), 
    # Refresh Token muddati (Hozirgi: 7 kun)
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7), 
    # Refresh Token yangilanganda eskisini o'chirish
    'ROTATE_REFRESH_TOKENS': True, 
    # Yangilangandan keyin eski Refresh Tokenni qora ro'yxatga kiritish
    'BLACKLIST_AFTER_ROTATION': True, 
    # Autentifikatsiya sarlavhasi turi
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
}

# ===============================
# 6. CORS Sozlamalari
# ===============================

# Barcha domenlardan APIga kirishga ruxsat beradi (Rivojlanish uchun).
# Productionda ma'lum domenlar ro'yxatini ko'rsatish tavsiya etiladi (CORS_ALLOWED_ORIGINS).
CORS_ALLOW_ALL_ORIGINS = True