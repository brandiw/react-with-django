from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

# urlpatterns = [
#     #url(r'^', ReactAppView.get, name="get"),
#     url(r'^', TemplateView.as_view(template_name="main.html")),
# ]

from my_app.views import ReactAppView

urlpatterns = [
    url(r'^', ReactAppView.as_view()),
]
