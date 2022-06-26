from django.urls import path
from . import views

urlpatterns = [  # отслеживание различных урлов
    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('cam', views.livefe, name='cam'),
]

