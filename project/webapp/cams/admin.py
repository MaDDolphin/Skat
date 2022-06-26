from django.contrib import admin
from .models import Webcam
from .models import Detections

admin.site.register(Webcam)
admin.site.register(Detections)
# Register your models here.
