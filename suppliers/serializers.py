from rest_framework import serializers
from .models import Supplier

class SupplierSerializer(serializers.ModelSerializer):
    """
    Yetkazib beruvchi modelini API orqali boshqarish uchun serializer.
    """
    supplier_type_display = serializers.CharField(source='get_supplier_type_display', read_only=True)
    
    class Meta:
        model = Supplier
        fields = (
            'id', 'name', 'contact_person', 'email', 'phone_number', 
            'address', 'supplier_type', 'supplier_type_display', 'is_active', 
            'created_at', 'updated_at'
        )
        read_only_fields = ('created_at', 'updated_at')