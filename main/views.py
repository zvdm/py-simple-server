import re

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.utils.html import escape
from django.views.generic.base import TemplateView, View

from main.models import Email, Press


class IndexView(TemplateView):
    """Render the main index page"""

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs) | {"maps_api_key": settings.MAPS_API_KEY}


class PressView(View):
    """Get all relevant press"""

    def get(self, request):
        limit = int(request.GET.get("limit", "5"))
        return JsonResponse({"press": list(Press.objects.order_by("-pk").values()[:limit])})


class SendEmailView(View):
    """Send a default reply in response to an appeal"""

    def post(self, request):
        sender, msg = escape(request.POST.get("sender")), escape(request.POST.get("msg"))
        email = request.POST.get("email")
        if not sender or not msg or not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            return HttpResponseBadRequest()
        if x_forwarded_for := request.META.get("HTTP_X_FORWARDED_FOR"):
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        email = Email.objects.create(
            sender_ip=ip,
            sender_name=sender,
            reply_email=email,
            message=msg,
        )
        email.email_send()
        return HttpResponse()
