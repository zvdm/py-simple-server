from django.contrib import admin

from .models import Email, Press


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ("id", "sender_name", "reply_email", "created_timestamp", "sender_ip")
    list_filter = ("created_timestamp",)


@admin.register(Press)
class PressAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "source", "created_timestamp")
    list_filter = ("created_timestamp",)
    readonly_fields = ("created_timestamp",)
