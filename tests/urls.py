from django.conf.urls import include, url
from django.views.generic import TemplateView


urlpatterns = [
    url(r"^test$", TemplateView.as_view(template_name="index.html"))
]