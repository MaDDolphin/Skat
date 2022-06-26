from django.urls import path
from . import views

urlpatterns = [  # отслеживание различных урлов
    path('', views.cam_list, name='cams'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.CamsDetailView.as_view(), name='cams-detail'),
    path('<int:pk>/update', views.CamsUpdateView.as_view(), name='cams-update'),
    path('<int:pk>/delete', views.CamsDeleteView.as_view(), name='cams-delete'),
]
