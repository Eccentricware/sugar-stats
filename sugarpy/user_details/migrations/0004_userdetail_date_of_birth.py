# Generated by Django 3.2.7 on 2021-10-29 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0003_auto_20211029_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]