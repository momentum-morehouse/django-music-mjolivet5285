from django import forms
from .models import Album

class albumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'artist_name',
            'title',
            'date_released',
        ]
        #widgets = {'birthday': forms.SelectDateWidget()
        #}



