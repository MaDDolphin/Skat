from django.urls import path
from . import views

urlpatterns = [  # отслеживание различных урлов
    path('', views.archive, name='detections'),
    path('<int:pk>/delete', views.DetectionDeleteView.as_view(), name='detection-delete'),
]
