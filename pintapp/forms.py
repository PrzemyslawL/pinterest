from django import forms
from pintapp.models import Photo

class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['likes']