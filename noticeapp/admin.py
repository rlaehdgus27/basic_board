from django.contrib import admin
from noticeapp.models import Notice


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):

    list_display = ("title", "type")

    list_filter = ("type",)
