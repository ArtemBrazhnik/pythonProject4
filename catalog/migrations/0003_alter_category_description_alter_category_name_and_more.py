# Generated by Django 5.1 on 2024-08-28 20:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.TextField(
                blank=True, null=True, verbose_name="Описание категории"
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                max_length=50, verbose_name="Наименование категории"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="categories",
                to="catalog.category",
                verbose_name="Категория",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateField(blank=True, null=True, verbose_name="Дата создания"),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(
                blank=True, null=True, verbose_name="Описание продукта"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(default=False, verbose_name="Опубликовано"),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=50, verbose_name="Наименование продукта"),
        ),
        migrations.AlterField(
            model_name="product",
            name="photo",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="product/photo",
                verbose_name="Изображение",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.IntegerField(blank=True, null=True, verbose_name="Цена"),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateField(
                blank=True, null=True, verbose_name="Дата последнего изменения"
            ),
        ),
        migrations.AlterField(
            model_name="version",
            name="is_version_active",
            field=models.BooleanField(default=False, verbose_name="Активная версия"),
        ),
        migrations.AlterField(
            model_name="version",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="versions",
                to="catalog.product",
                verbose_name="Продукт",
            ),
        ),
        migrations.AlterField(
            model_name="version",
            name="version_name",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Название версии"
            ),
        ),
        migrations.AlterField(
            model_name="version",
            name="version_number",
            field=models.CharField(
                blank=True, max_length=10, null=True, verbose_name="Номер версии"
            ),
        ),
    ]
