from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=50, verbose_name="Заголовок")
    slug = models.CharField(max_length=50, verbose_name="Ссылка")
    description = models.TextField(verbose_name="Содержимое", blank=True, null=True)
    photo = models.ImageField(upload_to="product/photo", blank=True, null=True, verbose_name="Изображение (превью)")
    created_at = models.DateTimeField(blank=True, null=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    views = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
