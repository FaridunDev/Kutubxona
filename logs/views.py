from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import ActivityLog
from .serializers import ActivityLogSerializer
from accounts.models import User
from rest_framework.exceptions import PermissionDenied

class IsAdminUser(IsAuthenticated):
    """
    Faqat Administratorga ruxsat berish.
    """
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        
        return request.user.role == User.Roles.ADMIN

class ActivityLogListView(generics.ListAPIView):
    """
    Barcha harakat jurnallarini ko'rish (Faqat ADMIN uchun).
    """
    queryset = ActivityLog.objects.all().select_related('user').order_by('-timestamp')
    serializer_class = ActivityLogSerializer
    permission_classes = [IsAdminUser]

class ActivityLogDetailView(generics.RetrieveAPIView):
    """
    Bitta harakat jurnalini ko'rish (Faqat ADMIN uchun).
    """
    queryset = ActivityLog.objects.all().select_related('user')
    serializer_class = ActivityLogSerializer
    permission_classes = [IsAdminUser]