from django.urls import path
from noticeapp.views import NoticeCreateView, NoticeListView, NoticeDetailView, NoticeUpdateView, NoticeDeleteView

app_name = "noticeapp"

urlpatterns = [
    path("create/", NoticeCreateView.as_view(), name="create"),
    path("list/", NoticeListView.as_view(), name="list"),
    path("detail/<int:pk>", NoticeDetailView.as_view(), name="detail"),
    path("update/<int:pk>", NoticeUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", NoticeDeleteView.as_view(), name="delete")
]

