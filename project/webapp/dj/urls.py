"""dj URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  # отслеживание различных урлов
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('cams/', include('cams.urls')),
    path('detections/', include('detections.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
