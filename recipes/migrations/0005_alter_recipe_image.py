# Generated by Django 4.2.6 on 2023-10-31 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, default='cook.jpg', upload_to='images'),
        ),
    ]