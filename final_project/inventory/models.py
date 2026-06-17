from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True, verbose_name="Номер телефона")
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    position = models.CharField(max_length=100, blank=True, null=True, verbose_name="Должность")

    def __str__(self):
        return f"{self.username} ({self.position or 'Сотрудник'})"


class Device(models.Model):
    STATUS_CHOICES = [
        ('active', 'В работе'),
        ('repair', 'Ремонт'),
        ('retired', 'Списано'),
    ]

    name = models.CharField(max_length=200, verbose_name="Наименование")
    inventory_number = models.CharField(max_length=50, unique=True, verbose_name="Инвентарный номер")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active', verbose_name="Статус")
    purchase_date = models.DateField(verbose_name="Дата покупки")
    slug = models.SlugField(unique=True, verbose_name="Slug (ЧПУ)")

    class Meta:
        ordering = ['-purchase_date']
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"

    def __str__(self):
        return f"{self.name} [{self.inventory_number}]"