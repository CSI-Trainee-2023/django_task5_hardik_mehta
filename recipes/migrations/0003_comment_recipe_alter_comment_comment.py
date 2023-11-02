# Generated by Django 4.2.6 on 2023-10-31 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='recipe',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=100),
        ),
    ]