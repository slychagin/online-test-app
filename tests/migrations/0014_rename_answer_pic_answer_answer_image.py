# Generated by Django 4.1.4 on 2023-01-20 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0013_alter_answer_answer_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer_pic',
            new_name='answer_image',
        ),
    ]
