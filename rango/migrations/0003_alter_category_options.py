# Generated by Django 4.1 on 2023-02-04 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("rango", "0002_category_likes_category_views"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
    ]