from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование категории")
    description = models.TextField(verbose_name="Описание категории", blank=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование продукта")
    description = models.TextField(verbose_name="Описание продукта", blank=True, null=True)
    photo = models.ImageField(upload_to="product/photo", blank=True, null=True, verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name="Категория", null=True, blank=True, related_name="categories")
    price = models.IntegerField(blank=True, null=True, verbose_name="Цена")
    created_at = models.DateField(blank=True, null=True, verbose_name="Дата создания")
    updated_at = models.DateField(blank=True, null=True, verbose_name="Дата последнего изменения")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Владелец", blank=True, null=True, related_name="products")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]
        permissions = [
            ('can_edit_product_description', 'Can edit product description'),
            ('can_edit_product_category', 'Can edit product category'),
            ('can_cancel_publication', 'Can cancel publication of product'),
        ]


    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(Product, related_name="versions", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Продукт")
    version_number = models.CharField(max_length=10, verbose_name="Номер версии", null=True, blank=True)
    version_name = models.CharField(max_length=100, verbose_name="Название версии", null=True, blank=True)
    is_version_active = models.BooleanField(default=False, verbose_name="Активная версия")

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["version_number", "version_name"]

    def __str__(self):
        return self.version_name
