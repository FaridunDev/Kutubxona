# books/models.py

from django.db import models
from accounts.models import User 

class Book(models.Model):
    """
    Kutubxonadagi har bir kitob haqidagi ma'lumotlar.
    """
    
    # ------------------ Asosiy Ma'lumotlar ------------------
    title = models.CharField(max_length=255, verbose_name="Kitob nomi")
    author = models.CharField(max_length=255, verbose_name="Muallif")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN") 
    publication_year = models.PositiveSmallIntegerField(verbose_name="Nashr yili")
    description = models.TextField(blank=True, null=True, verbose_name="Tavsif")


    class BookGenres(models.TextChoices):
        FICTION = "fiction", "Badiiy Adabiyot"
        SCIENCE = "science", "Ilmiy"
        HISTORY = "history", "Tarix"
        TECH = "tech", "Texnologiya/Dasturlash"
        CHILDREN = "children", "Bolalar Adabiyoti"
        OTHER = "other", "Boshqa"
        
    genre = models.CharField(
        max_length=50,
        choices=BookGenres.choices,
        default=BookGenres.FICTION,
        verbose_name="Janr"
    )
    
    added_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='books_added',
        verbose_name="Kiritdi"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
    
    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"
        unique_together = ('title', 'author', 'publication_year')