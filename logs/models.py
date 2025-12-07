from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from accounts.models import User

class ActivityLog(models.Model):
    """
    Tizimdagi muhim foydalanuvchi harakatlari va ob'ekt o'zgarishlarini qayd etish.
    """
    
    user = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='activity_logs',
        verbose_name="Foydalanuvchi"
    )
    

    class ActionTypes(models.TextChoices):
        CREATE = "create", "Yaratish"
        UPDATE = "update", "Yangilash"
        DELETE = "delete", "O'chirish"
        LOGIN = "login", "Kirish"
        LOGOUT = "logout", "Chiqish"
        BORROW = "borrow", "Qarzga berish"
        RETURN = "return", "Qaytarish"
        
    action_type = models.CharField(
        max_length=20,
        choices=ActionTypes.choices,
        verbose_name="Harakat turi"
    )

    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Sana va vaqt")
    content_type = models.ForeignKey(
        ContentType, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name="Ob'ekt turi"
    )
    object_id = models.PositiveIntegerField(
        null=True, 
        blank=True,
        verbose_name="Ob'ekt ID"
    )
    content_object = GenericForeignKey('content_type', 'object_id')
    changes = models.JSONField(
        null=True, 
        blank=True,
        verbose_name="O'zgarishlar"
    )
    
    description = models.CharField(max_length=255, verbose_name="Tavsif")

    def __str__(self):
        obj_info = f" ({self.content_object})" if self.content_object else ""
        return f"{self.user.username} - {self.get_action_type_display()} {obj_info} at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Harakat Jurnali"
        verbose_name_plural = "Harakat Jurnallari"
        ordering = ['-timestamp'] 