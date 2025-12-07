from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Supplier
from .serializers import SupplierSerializer
from accounts.models import User

class IsLibrarianOrInventoryManager(IsAuthenticated):
    """
    Faqat kutubxonachi, zaxira menejeri yoki administratorga ruxsat berish.
    """
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
            
        return request.user.role in [
            User.Roles.LIBRARIAN, 
            User.Roles.INVENTORY_MANAGER, 
            User.Roles.ADMIN
        ]

class SupplierListCreateView(generics.ListCreateAPIView):
    """
    Yetkazib beruvchilar ro'yxatini ko'rish (List) va yangi yetkazib beruvchi qo'shish (Create).
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsLibrarianOrInventoryManager]


class SupplierDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Bitta yetkazib beruvchini ko'rish (Retrieve), yangilash (Update) va o'chirish (Destroy).
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsLibrarianOrInventoryManager]