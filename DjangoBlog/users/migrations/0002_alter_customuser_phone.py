# Generated by Django 4.2.4 on 2023-08-24 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(max_length=11, unique=True, verbose_name='phone'),
        ),
    ]
