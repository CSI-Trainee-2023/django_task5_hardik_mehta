from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    auther = models.ForeignKey(User,on_delete=models.CASCADE)

    image = models.ImageField(upload_to='images',blank=True,null=True, default ='cooking.jpg')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("recipes-detail", kwargs = {"pk":self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("recipes-detail",kwargs = {"pk":self.recipe.id})