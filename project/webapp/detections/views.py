from django.shortcuts import render
from cams.models import Detections
from django.contrib import auth
from .forms import DetectionForm
from django.views.generic import DetailView, ListView, UpdateView, DeleteView


def archive(request):
    detected = Detections.objects.all()
    return render(request, 'detections/archive.html', {'detected': detected})


class DetectionDeleteView(DeleteView):
    model = Detections
    success_url = '/detections'
    template_name = 'detections/archive-delete.html'

    form_class = DetectionForm
