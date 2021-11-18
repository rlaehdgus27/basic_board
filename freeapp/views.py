from django.db import models
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from freeapp.models import Free
from freeapp.forms import FreeCreationForm
from django.urls import reverse_lazy


class FreeCreateView(CreateView):
    model = Free
    form_class = FreeCreationForm
    template_name = "freeapp/create.html"
    success_url = reverse_lazy("freeapp:list")


class FreeListView(ListView):
    model = Free
    context_object_name = "free_list"
    template_name = "freeapp/list.html"
    paginate_by = 20


class FreeDetailView(DetailView):
    model = Free
    context_object_name = "target_free"
    template_name = "freeapp/detail.html"


class FreeUpdateView(UpdateView):
    model = Free
    context_object_name = "target_free"
    form_class = FreeCreationForm
    template_name = "freeapp/update.html"
    success_url = reverse_lazy("freeapp:list")


class FreeDeleteView(DeleteView):
    model = Free
    context_object_name = "target_free"
    template_name = "freeapp/delete.html"
    success_url = reverse_lazy("freeapp:list")
