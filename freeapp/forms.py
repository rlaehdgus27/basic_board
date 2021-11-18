from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from freeapp.models import Free


class FreeCreationForm(ModelForm):
    class Meta:
        model = Free
        fields = ["title", "content", "image"]
