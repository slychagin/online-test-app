# Generated by Django 4.1.4 on 2023-01-20 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0008_alter_answer_answer_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_pic',
            field=models.ImageField(default='../default.jpg', upload_to='photos/answers', verbose_name='Фото ответа'),
        ),
    ]
