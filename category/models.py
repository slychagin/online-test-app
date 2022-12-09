from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Create category tabl in database"""
    objects = models.Manager()

    category_name = models.CharField(max_length=50, unique=True, verbose_name='Наименование категории')
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    category_image = models.ImageField(upload_to='photos/categories', blank=True, verbose_name='Фото категории')

    class Meta:
        """Show correct plural name"""
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def get_url(self):
        """
        Get category url to use in navbar
        :return: url for particular category
        """
        return reverse('test_by_category', args=[self.slug])

    def __str__(self):
        """Show category name in admin panel in string format"""
        return self.category_name
