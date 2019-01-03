from django.shortcuts import render
from django.views import View
from pintapp.models import Photo
from pintapp.forms import AddPhotoForm

# Create your views here.
class MainView(View):
    def get(self, request):
        photos = Photo.objects.all().order_by('-id')[:10]
        form = AddPhotoForm
        ctx = {
            'photos': photos,
            'form': form
        }
        return render(request, 'index.html', ctx)
    def post(self, request):
        form = AddPhotoForm(request.POST, request.FILES)

        if form.is_valid():
            photo = form.save()
            photos = Photo.objects.all().order_by('-id')[:10]
            return render(request, 'index.html', {'photos': photos, 'form': form})
        else:
            return render(request, 'index.html', {'form': form})

class ImageView(View):
    def get(self, request, id):
        photo = Photo.objects.get(id=id)
        return render(request, 'image.html', {'photo': photo})