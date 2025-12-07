from rest_framework import permissions

class IsLibrarianOrReadOnly(permissions.BasePermission):
    """
    Kutubxonachi (LIBRARIAN) yoki Administrator ruxsat berilganlar.
    Qolganlar faqat o'qishlari mumkin.
    """

    def has_permission(self, request, view):
        # GET, HEAD, OPTIONS so'rovlari uchun barchaga ruxsat
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Qolgan so'rovlar (POST, PUT, DELETE) uchun faqat kitobxonchi yoki admin ruxsat beriladi
        if request.user.is_authenticated:
            return request.user.role in ['librarian', 'admin', 'inventory_manager']
        
        return False

class IsOwnerOrLibrarian(permissions.BasePermission):
    """
    Faqat ob'ekt egasiga yoki LIBRARIAN/ADMIN ga ruxsat berilgan.
    """
    def has_object_permission(self, request, view, obj):
        # GET, HEAD, OPTIONS so'rovlari uchun barchaga ruxsat
        if request.method in permissions.SAFE_METHODS:
            return True

        # Qolgan so'rovlar uchun:
        # 1. Ob'ekt egasi (Kitobni qo'shgan foydalanuvchi)
        if obj.added_by == request.user:
            return True
        
        # 2. Yoki Kutubxonachi/Admin/Inventory Manager
        return request.user.role in ['librarian', 'admin', 'inventory_manager']