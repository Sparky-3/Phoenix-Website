from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic.base import TemplateView

app_name = "core"

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name='home'),
    path("admin/", admin.site.urls),
]