from django.urls import path
from .views import *
from django.views.generic import TemplateView


urlpatterns = [
    path('fbv-index', indexview, name='fbv-test'), # function base view
    path('cbv-index', TemplateView.as_view(template_name="index.html", extra_context={"name": "ali"})),
 # class base view
]