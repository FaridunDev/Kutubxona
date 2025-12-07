from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import ContentModeration
from .serializers import ContentModerationSerializer
from accounts.models import User
from django.utils import timezone

class IsModeratorOrAdmin(IsAuthenticated):
    """
    Faqat Moderator yoki Administratorga ruxsat berish.
    """
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
            
        return request.user.role in [
            User.Roles.MODERATOR, 
            User.Roles.ADMIN
        ]

class ContentModerationListCreateView(generics.ListCreateAPIView):
    """
    Barcha nazorat ob'ektlari ro'yxatini ko'rish va yangi nazorat ob'ektini yaratish.
    """
    queryset = ContentModeration.objects.all().select_related('moderated_by')
    serializer_class = ContentModerationSerializer
    permission_classes = [IsModeratorOrAdmin]
    
    def perform_create(self, serializer):
        serializer.save(moderated_by=self.request.user)


class ContentModerationDetailUpdateView(generics.RetrieveUpdateDestroyAPIView):
    """
    Bitta nazorat ob'ektini ko'rish, yangilash (tasdiqlash/rad etish) va o'chirish.
    """
    queryset = ContentModeration.objects.all()
    serializer_class = ContentModerationSerializer
    permission_classes = [IsModeratorOrAdmin]
    
    def perform_update(self, serializer):
        if 'status' in serializer.validated_data:
            serializer.save(
                moderated_by=self.request.user,
                moderated_at=timezone.now()
            )
        else:
            serializer.save()