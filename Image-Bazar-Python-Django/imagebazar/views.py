from django.http import HttpResponse
from django.shortcuts import render, redirect
from myapp.models import Category,Image


def show_about_page(request):
    print("About Page Request")
    name = "Neeraj is coding"
    link = "https://youtube.com"
    data = {
        'name' : name,
        'link' : link
    }
    #return HttpResponse("<h1>This is about page</h1>")
    return render(request, "about.html", data)

def show_home_page(request):
    cats = Category.objects.all()
    images = Image.objects.all()
    data = {
        'images':images,
        'cats': cats
    }
    return render(request,'home.html', data)


def show_category_page(request, cid):
    # print(cid)
    cats = Category.objects.all()
    category = Category.objects.get(pk=cid)
    # print(cat)
    images = Image.objects.filter(cat=category)              # left cat is taking from models.py
    data = {
        'images':images,
        'cats': cats
    }
    return render(request,'home.html', data)


def home(request):
    return redirect('/home')