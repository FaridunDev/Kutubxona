from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Roles(models.TextChoices):
        STUDENT = "student", "Student"
        TEACHER = "teacher", "Teacher"
        LIBRARIAN = "librarian", "Librarian"
        INVENTORY_MANAGER = "inventory_manager", "Inventory Manager"
        MODERATOR = "moderator", "Moderator"
        REVIEWER = "reviewer", "Reviewer"
        SECURITY = "security", "Security"
        SUPPLIER = "supplier", "Supplier"
        ADMIN = "admin", "Admin"

    role = models.CharField(
        max_length=50,
        choices=Roles.choices,
        default=Roles.STUDENT
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
