from cams.models import Detections
from django.forms import ModelForm, TextInput, Textarea, DateTimeField, ImageField


class DetectionForm(ModelForm):
    class Meta:
        model = Detections
        fields = ['cam_name', 'cam_link', 'date', 'detected_frame']
        # widgets = {
        #     'cam_name': TextInput(attrs={
        #         'class': "form-control",
        #         'placeholder': "Название камеры"
        #     }),
        #     'cam_link': Textarea(attrs={
        #         'class': "form-control",
        #         'placeholder': "Ссылка на камеру"
        #     }),
        #     'date': DateTimeField(attrs={
        #         'class': "form-control",
        #         'placeholder': "Дата"
        #     }),
        #     'detected_frame': ImageField(attrs={
        #         'class': "form-control",
        #         'placeholder': "Дата"
        #     }),
        # }
