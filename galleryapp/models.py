from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=200, null=False)
    content = models.TextField(null=False)
    image = models.ImageField(upload_to="%Y/%m/%d")
    create_at = models.DateField(auto_now_add=True)
