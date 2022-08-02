from django.urls import path
from . import views

urlpatterns = [
    path('cep/<cep>',views.api_cep)
]