from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """
    Kitob modelini API orqali boshqarish uchun serializer.
    """
    added_by_username = serializers.CharField(source='added_by.username', read_only=True)
    
    class Meta:
        model = Book
        fields = (
            'id', 'title', 'author', 'isbn', 
            'publication_year', 'genre', 'description',
            'added_by', 'added_by_username', 'created_at'
        )
        read_only_fields = ('added_by', 'created_at', 'updated_at')