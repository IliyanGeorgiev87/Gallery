from django.shortcuts import render

# Create your views here.

def gallery(request):
    return render(request, 'photoshare/gallery.html')

def addPhoto(request):
    return render(request, 'photoshare/add.html')

def viewPhoto(request, pk):
    return render(request, 'photoshare/photo.html')