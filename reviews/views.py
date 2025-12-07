from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializers import ReviewSerializer
from .permissions import IsOwnerOrReadOnly
from books.models import Book

class ReviewListCreateView(generics.ListCreateAPIView):
    """
    Sharhlar ro'yxatini ko'rish (List) va yangi sharh qo'shish (Create).
    Sharhlar ma'lum bir kitobga bog'langan holda ko'rsatiladi.
    """
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated] 
    
    def get_queryset(self):
        book_pk = self.kwargs.get('book_pk')
        if book_pk:
            return Review.objects.filter(book_id=book_pk).select_related('user', 'book')
        return Review.objects.all().select_related('user', 'book') 
        
    def perform_create(self, serializer):
        book_pk = self.kwargs.get('book_pk')
        book = Book.objects.get(pk=book_pk) 
        
        serializer.save(user=self.request.user, book=book)


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Bitta sharhni ko'rish (Retrieve), yangilash (Update) va o'chirish (Destroy).
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]