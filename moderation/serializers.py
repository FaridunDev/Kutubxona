from rest_framework import serializers
from .models import ContentModeration
from django.contrib.contenttypes.models import ContentType

class ContentModerationSerializer(serializers.ModelSerializer):
    """
    Kontent Nazorati obyektlari uchun serializer.
    """
    moderated_by_username = serializers.ReadOnlyField(source='moderated_by.username')
    content_object_repr = serializers.SerializerMethodField() 

    class Meta:
        model = ContentModeration
        fields = (
            'id', 'content_type', 'object_id', 'content_object_repr',
            'status', 'notes', 'moderated_by', 'moderated_by_username', 
            'created_at', 'moderated_at'
        )
        read_only_fields = ('content_type', 'object_id', 'moderated_by')
        
    def get_content_object_repr(self, obj):
        if obj.content_object:
            return str(obj.content_object)
        return 

    def validate(self, data):
        if self.instance is None:
            if 'content_type' not in data or 'object_id' not in data:
                 raise serializers.ValidationError(
                )
        return data