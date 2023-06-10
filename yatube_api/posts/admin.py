from django.contrib import admin

from .models import Comment, Group, Post

MAX_MESS_SIZE = 30  # Максимальный размер выводимого текста, при создании поста


class PostAdmin(admin.ModelAdmin):
    """
    Класс пост-админ
    Интерфейс администратора для списка постов.
    """

    list_display = ('pk', 'text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'

    def __str__(self) -> str:
        return self.text[:MAX_MESS_SIZE]


admin.site.register(Post, PostAdmin)
admin.site.register(Group)
admin.site.register(Comment)
