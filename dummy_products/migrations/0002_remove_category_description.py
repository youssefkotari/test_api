# Generated by Django 5.0 on 2024-04-28 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dummy_products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
    ]