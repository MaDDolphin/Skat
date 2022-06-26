from django.apps import AppConfig

# глобальные настройки для приложения


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
