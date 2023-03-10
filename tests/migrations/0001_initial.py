# Generated by Django 4.1.4 on 2022-12-15 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=255, unique=True, verbose_name='Наименование теста')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('test_image', models.ImageField(upload_to='photos/tests', verbose_name='Фото теста')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменений')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.test', verbose_name='Наименование теста')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200, verbose_name='Ответ')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Верно')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.question', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
