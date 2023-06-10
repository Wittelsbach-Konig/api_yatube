from django.apps import AppConfig


class PostsConfig(AppConfig):
    """Класс пост-конфиг
    Описание настроек приложения Posts
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
