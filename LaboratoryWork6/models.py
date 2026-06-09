from django.db import models
from django.utils import timezone

class Car(models.Model):
    brand = models.CharField(max_length=100, verbose_name="Марка")
    model = models.CharField(max_length=100, verbose_name="Модель")
    year = models.IntegerField(verbose_name="Год выпуска")
    price = models.DecimalField(max_length=10, max_digits=12, decimal_places=2, verbose_name="Цена")
    is_available = models.BooleanField(default=True, verbose_name="В наличии")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название отдела")

    def __str__(self):
        return self.name

class Employee(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    position = models.CharField(max_length=100, verbose_name="Должность")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees', verbose_name="Отдел")

    def __str__(self):
        return self.full_name

class Device(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    serial_number = models.CharField(max_length=100, unique=True, verbose_name="Серийный номер")
    purchase_date = models.DateField(verbose_name="Дата покупки")

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),
    ]
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft', verbose_name="Статус")

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=200)

class Author(models.Model):
    name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="Slug")

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles', verbose_name="Категория")

    def __str__(self):
        return self.title
