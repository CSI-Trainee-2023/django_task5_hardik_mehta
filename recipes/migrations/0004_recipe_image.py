# Generated by Django 4.2.6 on 2023-10-31 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_comment_recipe_alter_comment_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
