# Generated by Django 3.2.1 on 2021-06-05 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cams', '0003_alter_detections_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detections',
            name='title',
        ),
    ]
