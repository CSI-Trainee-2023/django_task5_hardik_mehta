from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from . import models
from django.urls import reverse_lazy

# Create your 
def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes' : recipes
    }
    return render(request,"recipes/home.html",context)


class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'


#class RecipeDetailView(DetailView):
    #model = models.Recipe

def recipeDetailView(request,pk):
    recipe = models.Recipe.objects.get(id=pk)
    
    comment=models.Comment.objects.filter(recipe=pk)
    
    context = {
        'object' : recipe,
        'comments':comment
    }
    
    return render(request,"recipes/recipe_detail.html",context)


def about(request):
    return render(request,"recipes/about.html",{'title':'about us page'})
   

class RecipeCreateView(LoginRequiredMixin,CreateView):
    model = models.Recipe
    fields = ['title','description','image']

    def form_valid(self,form):
        form.instance.auther = self.request.user
        return super().form_valid(form)
    



#for updation of recipe
class RecipeUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = models.Recipe
    fields = ['title','description','image']


    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.auther

    def form_valid(self,form):
        form.instance.auther = self.request.user
        return super().form_valid(form)
    



class RecipeDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView,):
    model = models.Recipe
    success_url = reverse_lazy('recipes-home')


    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.auther


def comment(request,id):
    comments = models.Comment.objects.all()
    context = {
        'comments' : comments
    }
    return render(request,"recipes/recipe_detail.html",context)


class CommentCreate(LoginRequiredMixin,CreateView):
    model = models.Comment
    fields = ['comment']
    def form_valid(self,form,**kwargs):
        recipe=get_object_or_404(models.Recipe,pk=self.kwargs.get('pk'))
        form.instance.recipe = recipe
        return super().form_valid(form)

    #success_url = reverse_lazy('recipes-detail')



class CommentView(ListView):
    model = models.Comment
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'comments'
