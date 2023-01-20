from django.db import models
from django.urls import reverse
from accounts.models import Account
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

    def get_url(self):
        """Get reverse url for particular test"""
        return reverse('test_description', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.test_name


class Question(models.Model):
    """Create question model in database"""
    objects = models.Manager()

    question = models.TextField(verbose_name='Вопрос')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='Наименование теста')

    class Meta:
        """Define how plural form looks in admin panel"""
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question


class Answer(models.Model):
    """Create answer model in database"""
    objects = models.Manager()

    answer = models.CharField(max_length=200, verbose_name='Ответ')
    answer_image = models.ImageField(upload_to='photos/answers', default='default.jpg', verbose_name='Фото ответа')
    is_correct = models.BooleanField(default=False, verbose_name='Верно')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')

    class Meta:
        """Define how plural form looks in admin panel"""
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.answer


class Results(models.Model):
    """Create results model in database"""
    objects = models.Manager()

    user = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Пользователь')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='Тест')
    correct_answer_count = models.IntegerField(verbose_name='Кол-во верных ответов')
    wrong_answer_count = models.IntegerField(verbose_name='Кол-во неверных ответов')
    correct_answer_percent = models.CharField(max_length=10, null=True, verbose_name='Процент правильных ответов')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата прохождения теста')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата повторного прохождения теста')

    def __str__(self):
        return self.test.test_name

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
