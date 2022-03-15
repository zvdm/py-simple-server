from django.urls import path

from main.views import IndexView, PressView, SendEmailView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("press/", PressView.as_view(), name="get-press"),
    path("send-email/", SendEmailView.as_view(), name="send-email"),
]
