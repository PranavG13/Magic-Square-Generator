from django.urls import path
from . import views

urlpatterns = [
    path('', views.magic_square_view, name='generate_square'),
]
