# Generated by Django 4.2.5 on 2023-09-29 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
