from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from accounts.models import User

class ContentModeration(models.Model):
    """
    Sharhlar yoki boshqa foydalanuvchi kontentini nazorat qilish va holatini saqlash.
    """
    content_type = models.ForeignKey(
        ContentType, 
        on_delete=models.CASCADE,
        verbose_name="Kontent turi"
    )
    object_id = models.PositiveIntegerField(verbose_name="Ob'ekt ID")
    content_object = GenericForeignKey('content_type', 'object_id')
    
    # ------------------ Holat ------------------
    class ModerationStatuses(models.TextChoices):
        PENDING = "pending", "Kutishda"        
        APPROVED = "approved", "Tasdiqlangan"  
        REJECTED = "rejected", "Rad etilgan"   
        FLAGGED = "flagged", "Belgilangan"
        
    status = models.CharField(
        max_length=20,
        choices=ModerationStatuses.choices,
        default=ModerationStatuses.PENDING,
        verbose_name="Holati"
    )

    # ------------------ Boshqaruv ------------------
    moderated_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='moderated_actions',
        verbose_name="Nazoratchi"
    )
    
    notes = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Nazoratchi eslatmalari"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    moderated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Moderation for {self.content_object} - {self.get_status_display()}"

    class Meta:
        verbose_name = "Kontent Nazorati"
        verbose_name_plural = "Kontent Nazoratlari"
        unique_together = ('content_type', 'object_id')