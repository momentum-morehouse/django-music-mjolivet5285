from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render 
from .models import Album
from .forms import AlbumForm
# Create your views here.


def index(request):
  albums = Album.objects.all()
  return render(request,'unchained_project/list_albums.html',{'albums':albums})

def add_album(request):
  if request.method == 'GET':
        form = AlbumForm()
  else:
      form = AlbumForm(data=request.POST)
      if form.is_valid():
          form.save()
          return redirect(to='list_albums')

  return render(request, "unchained_project/add_album.html", {"form": form})

def delete_album(request, pk):
  album = get_object_or_404(Album, pk=pk)
  if request.method == 'POST':
    album.delete()
    return redirect(to="list_albums")
  return render(request, "unchained_project/delete_album.html",
                  {"album": album})
  
def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=Album)
    else:
      form = AlbumForm(data=request.POST, instance=Album)
      if form.is_valid():
            form.save()
            return redirect(to='list_albums')

      