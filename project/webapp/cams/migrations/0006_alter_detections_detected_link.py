# Generated by Django 3.2.1 on 2021-06-06 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cams', '0005_alter_detections_detected_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detections',
            name='detected_link',
            field=models.ImageField(upload_to='detections', verbose_name='Cрабатывание'),
        ),
    ]