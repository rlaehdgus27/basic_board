from core.views import home, assignment, service
from django.urls import path

app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path("assignment/", assignment, name="assignment"),
    path("service/", service, name="service")
]
