# borrowing/models.py

from django.db import models
from accounts.models import User
from inventory.models import BookCopy 
from datetime import timedelta
from django.utils import timezone 

# Standart qarzga berish muddati 
DEFAULT_LOAN_DAYS = 14
def get_default_expected_return_date():
    """Qaytarishning standart kutilayotgan sanasini hisoblaydigan funksiya."""
    return timezone.now().date() + timedelta(days=DEFAULT_LOAN_DAYS)

class Borrowing(models.Model):
    """
    Foydalanuvchi va qarzga olingan kitob nusxasi o'rtasidagi aloqa.
    """

    book_copy = models.ForeignKey(
        BookCopy, 
        on_delete=models.RESTRICT, # Kitob nusxasini qarzda bo'lsa o'chirishni cheklaydi
        related_name='borrowings',
        verbose_name="Qarzga olingan nusxa"
    )
    
    user = models.ForeignKey(
        User,
        on_delete=models.RESTRICT, # Foydalanuvchi qarzda bo'lsa o'chirishni cheklaydi
        related_name='borrowed_books',
        verbose_name="Qarz oluvchi"
    )
    
    borrowed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='issued_borrowings',
        verbose_name="Qarz bergan xodim"
    )

    borrow_date = models.DateField(auto_now_add=True, verbose_name="Qarzga berilgan sana")
    expected_return_date = models.DateField(
        default=get_default_expected_return_date, 
        verbose_name="Kutilayotgan qaytarish sanasi"
    )
    
    actual_return_date = models.DateField(
        null=True, 
        blank=True, 
        verbose_name="Haqiqiy qaytarish sanasi"
    )

    # ------------------ Holat ------------------
    is_returned = models.BooleanField(default=False, verbose_name="Qaytarilgan")
    
    def __str__(self):
        return f"{self.user.username} borrowed {self.book_copy.book.title} on {self.borrow_date}"

    class Meta:
        verbose_name = "Qarzga berish"
        verbose_name_plural = "Qarzga berishlar"