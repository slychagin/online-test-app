from django.db import models
from category.models import Category


class Test(models.Model):
    """Create test model in database"""
    objects = models.Manager()

    test_name = models.CharField(max_length=255, unique=True, verbose_name='Наименование теста')
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    test_image = models.ImageField(upload_to='photos/tests', verbose_name='Фото теста')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменений')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        """Define how plural form looks in admin panel"""
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.test_name
