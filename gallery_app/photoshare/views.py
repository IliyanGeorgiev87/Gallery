from django.shortcuts import render
from .models import Category, Photo

# Create your views here.

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()

    context = {'categories': categories, 'photos': photos}
    
    return render(request, 'photoshare/gallery.html', context)

def addPhoto(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'photoshare/add.html', context)

def viewPhoto(request, pk):
    photos = Photo.objects.get(id=pk)
    return render(request, 'photoshare/photo.html', {'photo': photos})