from django.db import models
from datetime import datetime


class Webcam(models.Model):
    title = models.CharField('Название', max_length=50)
    link = models.TextField('Ссылка на камеру')

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return '/cams'

    class Meta:
        verbose_name = 'Камера'
        verbose_name_plural = 'Камеры'


class Detections(models.Model):
    cam_name = models.TextField('Название камеры', default='NULL')
    cam_link = models.TextField('id камеры', default='NULL')
    date = models.DateTimeField('Дата срабатывания', default=datetime.now, blank=True)
    detected_frame = models.ImageField('Cрабатывание', upload_to='detections')

    def __str__(self):
        return self.cam_name

    class Meta:
        verbose_name = 'Обнаружение'
        verbose_name_plural = 'Обнаружения'
