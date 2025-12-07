from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Borrowing
from .serializers import BorrowingCreateSerializer, BorrowingReturnSerializer
from accounts.models import User
from rest_framework.decorators import action

# Ruxsatnomalar: Faqat Kutubxonachi, Admin yoki Moderator qarzga berishi mumkin
class IsLibrarianOrAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and \
               request.user.role in [User.Roles.LIBRARIAN, User.Roles.ADMIN, User.Roles.MODERATOR]


class BorrowingListCreateView(generics.ListCreateAPIView):
    """
    Barcha qarzga berish amaliyotlari (Ro'yxat va Yaratish).
    """
    queryset = Borrowing.objects.all().select_related('book_copy', 'user', 'book_copy__book')
    permission_classes = [IsLibrarianOrAdmin]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BorrowingCreateSerializer
        return BorrowingCreateSerializer 

    def get_queryset(self):
        if self.request.user.role == User.Roles.ADMIN:
            return Borrowing.objects.all()
        return Borrowing.objects.filter(user=self.request.user)
        
    def perform_create(self, serializer):
        serializer.save(borrowed_by=self.request.user)


class BorrowingReturnView(generics.UpdateAPIView):
    """
    Kitobni qaytarish amaliyotini yakunlash (PATCH).
    """
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingReturnSerializer
    permission_classes = [IsLibrarianOrAdmin]
    http_method_names = ['patch'] 

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)