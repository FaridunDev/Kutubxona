from django.db import models
from accounts.models import User
from books.models import Book

class Review(models.Model):
    """
    Foydalanuvchi tomonidan kitobga berilgan sharh va reyting.
    """
    
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE, 
        related_name='reviews', 
        verbose_name="Kitob"
    )
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE, 
        related_name='reviews',
        verbose_name="Sharhlovchi"
    )


    rating = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 6)], 
        verbose_name="Reyting (1-5)"
    )
    
    comment = models.TextField(
        max_length=1000, 
        blank=True, 
        null=True, 
        verbose_name="Sharh matni"
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan sana")

    def __str__(self):
        return f"Review for {self.book.title} by {self.user.username} - {self.rating}/5"

    class Meta:
        verbose_name = "Sharh"
        verbose_name_plural = "Sharhlar"
        unique_together = ('book', 'user')