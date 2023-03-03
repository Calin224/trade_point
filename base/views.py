from django.contrib.auth import login
from django.shortcuts import render, redirect
from item.models import Category, Item

from .forms import SignupForm

# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)[0:10]
    categoies = Category.objects.all()
        
    return render(request, 'base/index.html', {
        'items': items,
        'categories': categoies,
    })

def contact(request):
    return render(request, 'base/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/login/')
    else:    
        form = SignupForm()
        
    return render(request, 'base/signup.html', {
        'form': form,
    })
