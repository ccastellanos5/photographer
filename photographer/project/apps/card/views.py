from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Image
from django.http import HttpResponse, Http404

def index(request):
    album = Album.objects.all()
    context={
        'album':album
    }

    
    return render(request, "index.html", context)
