from django.contrib import admin
from django.urls import path
from . import views

'app/model_viewtype'
'recipes/recipe_detail.html'


urlpatterns = [
    path('',views.RecipeListView.as_view(),name = 'recipes-home'),
    path('recipe/create/',views.RecipeCreateView.as_view(),name = 'recipes-create'),
    path('recipes/<int:pk>/',views.recipeDetailView,name = 'recipes-detail'),
    path('about/',views.about,name = 'recipes_about'),
    path('recipe/<int:pk>/update/',views.RecipeUpdateView.as_view(),name = 'recipes-update'),
    path('recipe/<int:pk>/delete/',views.RecipeDeleteView.as_view(),name = 'recipes-delete'),
    path('recipe/<int:pk>/comment/',views.CommentCreate.as_view(),name = 'recipes-comment'),
    path('recipe/<int:pk>/image/',views.CommentCreate.as_view(),name = 'recipes-image'),
]
