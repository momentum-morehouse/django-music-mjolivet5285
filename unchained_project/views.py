from django.shortcuts import render,redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm

# Create your views here.
def index(request):
  album = Album.objects.all()
  return render(request,'yeti_project/list_albums.html',{'album':album})

  # def add_album(request):
  #   if request.method == 'GET':
  #       form = AlbumForm()
  #   else:
  #       form = AlbumForm(data=request.POST)
  #       if form.is_valid():
  #           form.save()
  #           return render (to='list_albums')

  #   return render(request, "yeti_project/add_album.html", {"form": form})

    