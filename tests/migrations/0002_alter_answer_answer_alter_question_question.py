# Generated by Django 4.1.4 on 2022-12-10 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.CharField(max_length=200, verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(verbose_name='Вопрос'),
        ),
    ]
