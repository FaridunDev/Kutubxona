from rest_framework import serializers
from .models import ActivityLog

class ActivityLogSerializer(serializers.ModelSerializer):
    """
    Harakat Jurnali ob'ektlari uchun serializer.
    """
    user_username = serializers.ReadOnlyField(source='user.username')
    action_type_display = serializers.ReadOnlyField(source='get_action_type_display')
    content_object_repr = serializers.SerializerMethodField()
    
    class Meta:
        model = ActivityLog
        fields = (
            'id', 'user', 'user_username', 'action_type', 'action_type_display', 
            'timestamp', 'description', 'content_type', 'object_id', 
            'content_object_repr', 'changes'
        )
        read_only_fields = '__all__' 

    def get_content_object_repr(self, obj):
        """Tekshirilayotgan ob'ektning __str__ qiymatini qaytaradi."""
        if obj.content_object:
            return str(obj.content_object)
        return None