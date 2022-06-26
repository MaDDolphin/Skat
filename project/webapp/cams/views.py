from django.shortcuts import render, redirect
from .models import Webcam
from .models import Detections
from .forms import CamsForm
from django.views.generic import DetailView, ListView, UpdateView, DeleteView


def cam_list(request):
    cams = Webcam.objects.all()
    return render(request, 'cams/cams_home.html', {'cams': cams})


class CamsDetailView(DetailView):
    model = Webcam
    template_name = 'cams/details.view.html'
    context_object_name = 'cam'


class CamsUpdateView(UpdateView):
    model = Webcam
    template_name = 'cams/create.html'
    form_class = CamsForm


class CamsDeleteView(DeleteView):
    model = Webcam
    success_url = '/cams'
    template_name = 'cams/cams-delete.html'

    form_class = CamsForm


def create(request):
    error = ''
    if request.method == 'POST':
        form = CamsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cams')
        else:
            error = 'Форма была неверной'

    form = CamsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'cams/create.html', data)

