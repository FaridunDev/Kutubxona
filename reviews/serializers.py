from rest_framework import serializers
from .models import Review
from accounts.models import User
from books.models import Book

class ReviewSerializer(serializers.ModelSerializer):
    """
    Sharhlar va reytinglar uchun serializer.
    """
    user_username = serializers.ReadOnlyField(source='user.username')
    book_title = serializers.ReadOnlyField(source='book.title')

    class Meta:
        model = Review
        fields = (
            'id', 'book', 'book_title', 'user', 'user_username', 
            'rating', 'comment', 'created_at', 'updated_at'
        )
        read_only_fields = ('user',)
        
    def validate(self, data):
        if self.instance is None:
            user = self.context['request'].user
            book = data.get('book')
            
            if Review.objects.filter(user=user, book=book).exists():
                raise serializers.ValidationError(
                    "Siz allaqachon bu kitobga sharh qoldirgansiz. Uni tahrirlashingiz mumkin."
                )
        return data