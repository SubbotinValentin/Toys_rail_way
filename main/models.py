from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    price = models.IntegerField(default=True, verbose_name='Цена')
    stock = models.PositiveIntegerField(null=True)
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('prod', kwargs={'prod_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cat_slug', kwargs={'cat_slug': self.slug})