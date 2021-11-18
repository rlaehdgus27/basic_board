from django.db import models
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from galleryapp.models import Gallery
from galleryapp.forms import GalleryCreationForm
from django.urls import reverse_lazy


class GalleryCreateView(CreateView):
    model = Gallery
    form_class = GalleryCreationForm
    template_name = "galleryapp/create.html"
    success_url = reverse_lazy("galleryapp:list")


class GalleryListView(ListView):
    model = Gallery
    context_object_name = "gallery_list"
    template_name = "galleryapp/list.html"
    paginate_by = 20


class GalleryDetailView(DetailView):
    model = Gallery
    context_object_name = "target_gallery"
    template_name = "galleryapp/detail.html"


class GalleryUpdateView(UpdateView):
    model = Gallery
    context_object_name = "target_gallery"
    form_class = GalleryCreationForm
    template_name = "galleryapp/update.html"
    success_url = reverse_lazy("galleryapp:list")


class GalleryDeleteView(DeleteView):
    model = Gallery
    context_object_name = "target_gallery"
    template_name = "galleryapp/delete.html"
    success_url = reverse_lazy("galleryapp:list")
