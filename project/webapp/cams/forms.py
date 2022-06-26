from .models import Webcam
from django.forms import ModelForm, TextInput, Textarea


class CamsForm(ModelForm):
    class Meta:
        model = Webcam
        fields = ['title', 'link']

        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Название камеры"
            }),
            'link': Textarea(attrs={
                'class': "form-control",
                'placeholder': "Ссылка на камеру"
            }),
        }
