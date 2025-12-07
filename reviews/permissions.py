from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Faqat ob'ekt egasiga o'zgartirish/o'chirishga ruxsat berilgan.
    Boshqalar faqat o'qishlari mumkin.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user