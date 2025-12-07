from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from .permisions import IsLibrarianOrReadOnly,IsOwnerOrLibrarian

class BookListCreateView(generics.ListCreateAPIView):
    """
    Kitoblar ro'yxatini ko'rish (List) va yangi kitob qo'shish (Create).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # GET so'rovi barchaga ruxsat, POST esa faqat kerakli rollarga
    permission_classes = [IsAuthenticated, IsLibrarianOrReadOnly] 

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Bitta kitobni ko'rish (Retrieve), yangilash (Update) va o'chirish (Destroy).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrLibrarian]