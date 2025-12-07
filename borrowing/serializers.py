from rest_framework import serializers
from .models import Borrowing
from inventory.models import BookCopy, InventoryItem
from django.utils import timezone

class BorrowingCreateSerializer(serializers.ModelSerializer):
    """
    Yangi kitobni qarzga berish uchun Serializer (CREATE).
    """
    class Meta:
        model = Borrowing
        fields = ('id', 'book_copy', 'user', 'expected_return_date', 'borrow_date')
        read_only_fields = ('borrow_date', 'expected_return_date') 

    def validate(self, data):
        book_copy = data['book_copy']
        
        if book_copy.status != BookCopy.CopyStatuses.AVAILABLE:
            raise serializers.ValidationError(
                f"Bu nusxa hozirda qarzga berish uchun mavjud emas. Holati: {book_copy.get_status_display()}."
            )
        

        user_current_borrowings = Borrowing.objects.filter(user=data['user'], is_returned=False).count()
        MAX_BORROW_LIMIT = 3
        
        if user_current_borrowings >= MAX_BORROW_LIMIT:
            raise serializers.ValidationError(
                f"Foydalanuvchi allaqachon maksimal {MAX_BORROW_LIMIT} ta kitobni qarzga olgan."
            )

        return data
        
    def create(self, validated_data):
        borrowing = super().create(validated_data)
        book_copy = validated_data['book_copy']
        book_copy.status = BookCopy.CopyStatuses.ON_LOAN
        book_copy.save()
        inventory = book_copy.inventory_item
        inventory.available_stock -= 1
        inventory.on_loan += 1
        inventory.save()
        
        return borrowing


class BorrowingReturnSerializer(serializers.ModelSerializer):
    """
    Kitobni qaytarish amaliyoti uchun Serializer (UPDATE).
    """
    class Meta:
        model = Borrowing
        fields = ('id', 'actual_return_date', 'is_returned')
        read_only_fields = ('is_returned',) 
        
    def validate_actual_return_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Haqiqiy qaytarish sanasi kelajakdagi sana bo'lishi mumkin emas.")
        return value

    def update(self, instance, validated_data):
        if instance.is_returned:
            raise serializers.ValidationError("Bu qarz amaliyoti allaqachon yopilgan (kitob qaytarilgan).")
            
        instance.actual_return_date = validated_data.get('actual_return_date', timezone.now().date())
        instance.is_returned = True
        instance.save()
        
        book_copy = instance.book_copy
        book_copy.status = BookCopy.CopyStatuses.AVAILABLE
        book_copy.save()
        

        inventory = book_copy.inventory_item
        inventory.available_stock += 1
        inventory.on_loan -= 1
        inventory.save()
        
        return instance