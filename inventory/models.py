from django.db import models
from books.models import Book    # Kitob modelini import qilish
from accounts.models import User # User modelini import qilish 

class InventoryItem(models.Model):
    """
    Kitobning Kutubxonadagi umumiy zaxira holatini saqlaydi.
    Kitobning Book modelidagi umumiy ma'lumotlariga bog'lanadi.
    """
    book = models.OneToOneField(
        Book, 
        on_delete=models.CASCADE, 
        related_name='inventory', 
        verbose_name="Kitob"
    )
    total_stock = models.PositiveIntegerField(default=0, verbose_name="Umumiy zaxira")
    available_stock = models.PositiveIntegerField(default=0, verbose_name="Mavjud nusxalar")
    on_loan = models.PositiveIntegerField(default=0, verbose_name="Qarzda")
    last_updated_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='inventory_updates',
        verbose_name="So'nggi yangilagan xodim"
    )
    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inventory for: {self.book.title}"
    
    class Meta:
        verbose_name = "Zaxira Hisobi"
        verbose_name_plural = "Zaxira Hisoblari"

class BookCopy(models.Model):
    """
    Kitobning jismoniy bir nusxasini ifodalaydi.
    Qarzga berish (borrowing) amallari aynan shu model ustida bajariladi.
    """
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE, 
        related_name='copies', 
        verbose_name="Asosiy kitob"
    )
    inventory_item = models.ForeignKey(
        InventoryItem, 
        on_delete=models.CASCADE, 
        related_name='book_copies', 
        verbose_name="Zaxira obyekti"
    )
    


    accession_number = models.CharField(max_length=50, unique=True, verbose_name="Inventar raqami")
    class CopyStatuses(models.TextChoices):
        AVAILABLE = "available", "Mavjud"
        ON_LOAN = "on_loan", "Qarzga berilgan"
        MAINTENANCE = "maintenance", "Ta'mirlashda"
        LOST = "lost", "Yo'qolgan"
        
    status = models.CharField(
        max_length=20,
        choices=CopyStatuses.choices,
        default=CopyStatuses.AVAILABLE,
        verbose_name="Holati"
    )
    
    condition = models.CharField(max_length=100, default='Yaxshi', verbose_name="Jismoniy holat")
    shelf_location = models.CharField(max_length=50, verbose_name="Javonda joylashuvi")
    purchased_date = models.DateField(auto_now_add=True, verbose_name="Sotib olingan sana")


    def __str__(self):
        return f"Copy of {self.book.title} (ID: {self.accession_number}) - {self.get_status_display()}"
    
    class Meta:
        verbose_name = "Kitob Nusxasi"
        verbose_name_plural = "Kitob Nusxalari"