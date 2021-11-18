from django.db import models
from django.forms import ModelForm
from noticeapp.models import Notice


class NoticeCreationForm(ModelForm):
    class Meta:
        model = Notice
        fields = ["title", "type", "content"]
