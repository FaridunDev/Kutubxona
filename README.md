# 📚 Kutubxona API

**Kutubxona API** — bu Django REST Framework (DRF) orqali yaratilgan, rollarga asoslangan zamonaviy kutubxona boshqaruv tizimi. Loyiha kitoblar zaxirasini, qarz olish amaliyotlarini, sharhlarni, xodimlarni va tizimdagi harakatlarni (logs) samarali boshqarishga mo'ljallangan.

## 🌟 Asosiy Imkoniyatlar

* **Foydalanuvchini Boshqarish:** Maxsus `User` modeli (rolga asoslangan ruxsatnomalar bilan: Admin, Kutubxonachi, Moderator, Zaxira menejeri).
* **Kitob Zaxirasi:** Bibliografik ma'lumotlar (`Book`), har bir nusxaning holati/joylashuvi (`BookCopy`) va umumiy zaxira hisobi (`InventoryItem`).
* **Qarzga Berish (Borrowing):** Kitob nusxalarini qarzga berish, qaytarish va muddatni kuzatish (Borrowing limitlarini tekshirish bilan).
* **Sharhlar va Reytinglar (Reviews):** Foydalanuvchilar kitoblarga sharh va reyting bera olishi.
* **Nazorat (Moderation):** `GenericForeignKey` asosidagi universal nazorat tizimi orqali foydalanuvchi kontentini (masalan, Sharhlarni) tasdiqlash.
* **Harakat Jurnali (Logs):** Tizimdagi muhim harakatlarni (CREATE, UPDATE, BORROW, RETURN) kuzatish uchun `GenericForeignKey` asosidagi jurnal tizimi.
* **Yetkazib Beruvchilar (Suppliers):** Kitob yetkazib beruvchilar ma'lumotlarini boshqarish.
* **Xavfsizlik:** **JWT (JSON Web Token)** asosidagi xavfsiz autentifikatsiya.

---

## 🛠️ Texnologiyalar

| Kategoriya | Texnologiya | Izoh |
| :--- | :--- | :--- |
| **Backend Framework** | Python, **Django** | Tez va xavfsiz backend rivojlanish uchun. |
| **API** | **Django REST Framework (DRF)** | RESTful API yaratish uchun. |
| **Autentifikatsiya** | **Simple JWT** | Tokenlarga asoslangan xavfsiz kirish. |
| **Ma'lumotlar Bazasi** | **PostgreSQL** | Kuchli, ishonchli va kengaytiriluvchan ma'lumotlar bazasi. |
| **Hujjatlanma** | **drf-yasg** | Avtomatik Swagger/OpenAPI hujjatlari. |

---

## ⚙️ O'rnatish va Ishga Tushirish

### 1. Loyihani Klonlash va Muhitni Sozlash

```bash
# Loyihani klonlash
git clone [https://github.com/FaridunDev/Kutubxona.git](https://github.com/FaridunDev/Kutubxona.git)
cd Kutubxona

# Virtual muhit yaratish va aktivlash
python3 -m venv env
source env/bin/activate