from django.urls import path
from freeapp.views import FreeCreateView, FreeDeleteView, FreeDetailView, FreeListView, FreeUpdateView


app_name = "freeapp"

urlpatterns = [
    path("create/", FreeCreateView.as_view(), name="create"),
    path("list/", FreeListView.as_view(), name="list"),
    path("detail/<int:pk>", FreeDetailView.as_view(), name="detail"),
    path("update/<int:pk>", FreeUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", FreeDeleteView.as_view(), name="delete")
]
