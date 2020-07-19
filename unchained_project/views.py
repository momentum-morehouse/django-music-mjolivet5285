from django.shortcuts import render, redirect
from .models import Album
from .forms import albumForm
# Create your views here.
def index(request):
  albums = Album.objects.all()
  return render(request,'unchained_project/list_albums.html',{'albums':albums})

def add_album(request):
  if request.method == 'GET':
        form = albumForm()
  else:
      form = albumForm(data=request.POST)
      if form.is_valid():
          form.save()
          return redirect(to='list_albums')

  return render(request, "unchained_project/add_album.html", {"form": form})