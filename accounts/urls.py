# accounts/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserRegistrationView, LogoutView

urlpatterns = [
    # ------------------
    # Foydalanuvchi hisobi
    # ------------------
    path('register/', UserRegistrationView.as_view(), name='register'),
    
    # ------------------
    # Autentifikatsiya (JWT)
    # ------------------
    # Login (Access va Refresh tokenlarini olish)
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Access tokenini yangilash
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Logout (Refresh tokenni blacklisting qilish)
    path('logout/', LogoutView.as_view(), name='logout'),
]