from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # --- 3. Loyiha Ilovalari API URL manziliga ulandi ---
    
    # 3.1. Accounts (Foydalanuvchi va Registratsiya)
    path('api/accounts/', include('accounts.urls')), 
    
    # 3.2. Books (Kitob ma'lumotlari)
    path('api/books/', include('books.urls')),
    
    # 3.3. Inventory (Zaxira va Nusxalar)
    path('api/inventory/', include('inventory.urls')), 
    
    # 3.4. Borrowing (Qarzga berish va Qaytarish)
    path('api/borrowing/', include('borrowing.urls')), 
    
    # 3.5. Suppliers (Yetkazib beruvchilar)
    path('api/suppliers/', include('suppliers.urls')), 
    
    # 3.6. Reviews (Sharhlar)
    # Reviews ilovasi books ilovasining URL'iga bog'langan (books/<int:book_pk>/reviews)
    path('api/reviews/', include('reviews.urls')), 
    
    # 3.7. Moderation (Kontent nazorati)
    path('api/moderation/', include('moderation.urls')), 
    
    # 3.8. Logs (Harakat jurnali)
    path('api/logs/', include('logs.urls')), 
    
    # --- DRF ning brauzer orqali kirish uchun login/logout funksiyasi 
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]