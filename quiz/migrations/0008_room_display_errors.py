# Generated by Django 5.0.3 on 2024-04-28 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_rename_tupe_question_tupe_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='Display_errors',
            field=models.BooleanField(default=True, verbose_name='Отображать ошибки'),
        ),
    ]