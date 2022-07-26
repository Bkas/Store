from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm

# Create your views here.
def home(request):
    return render(request, "first.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def shop(request):
    return render(request, "shop.html")

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {"form":form})
