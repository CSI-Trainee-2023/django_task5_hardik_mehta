from django.shortcuts import render,redirect
from django.contrib import messages



from .import forms

# Create your views here.
def register(request):
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"{username},you're account have been created,please login")
            return redirect('user-login')
    else:
        form = forms.UserRegisterForm()
    return render(request,'users/register.html',{'form': form})


def profile(request):
    return render(request,'users/profile.html')
