from django.db import models
from django.forms import ModelForm
from galleryapp.models import Gallery


class GalleryCreationForm(ModelForm):
    class Meta:
        model = Gallery
        fields = ["title", "content", "image"]
