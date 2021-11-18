from django.contrib import admin
from galleryapp.models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):

    list_display = ("title", "image")
