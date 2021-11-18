from django.db import models


class Notice(models.Model):

    TYPE_CHOICE = (
        ("A.공지사항", "A.공지사항"),
        ("B.새소식", "B.새소식"),
        ("C.기타", "C.기타"),
    )

    title = models.CharField(max_length=200, null=False)
    type = models.CharField(
        max_length=20, choices=TYPE_CHOICE, null=True, blank=True)
    content = models.TextField(null=False)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
