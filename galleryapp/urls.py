from django.urls import path
from galleryapp.views import GalleryCreateView, GalleryDeleteView, GalleryDetailView, GalleryListView, GalleryUpdateView


app_name = "galleryapp"

urlpatterns = [
    path("create/", GalleryCreateView.as_view(), name="create"),
    path("list/", GalleryListView.as_view(), name="list"),
    path("detail/<int:pk>", GalleryDetailView.as_view(), name="detail"),
    path("update/<int:pk>", GalleryUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", GalleryDeleteView.as_view(), name="delete")
]
