from django.db import models

class Supplier(models.Model):
    """
    Kitoblarni kutubxonaga yetkazib beruvchi tashkilot yoki shaxs.
    """
    
    # ------------------ Asosiy Ma'lumotlar ------------------
    name = models.CharField(max_length=255, unique=True, verbose_name="Yetkazib beruvchi nomi")
    contact_person = models.CharField(max_length=150, blank=True, null=True, verbose_name="Bog'lanuvchi shaxs")
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True, verbose_name="Elektron pochta")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefon raqami")
    
    # ------------------ Manzil va Boshqa Ma'lumotlar ------------------
    address = models.TextField(blank=True, null=True, verbose_name="Manzil")

    class SupplierTypes(models.TextChoices):
        PUBLISHER = "publisher", "Nashriyot"
        DISTRIBUTOR = "distributor", "Distribyutor"
        BOOKSTORE = "bookstore", "Kitob do'koni"
        PRIVATE = "private", "Xususiy shaxs/Sovg'a"
        
    supplier_type = models.CharField(
        max_length=50,
        choices=SupplierTypes.choices,
        default=SupplierTypes.DISTRIBUTOR,
        verbose_name="Turi"
    )

    is_active = models.BooleanField(default=True, verbose_name="Faol")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Yetkazib beruvchi"
        verbose_name_plural = "Yetkazib beruvchilar"
        ordering = ['name']