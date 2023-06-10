from django.contrib.auth import get_user_model
from django.db import models


MAX_LEN_TO_STR = 200  # Максимальный размер строки
User = get_user_model()


class Group(models.Model):
    """Модель групп
    Атрибуты:
        title : Название
        slug : Уникальный фрагмент URL
        description : Описание
    """

    title = models.CharField('Название',
                             max_length=MAX_LEN_TO_STR,
                             help_text='Введите название группы')
    slug = models.SlugField('Уникальный фрагмент URL',
                            unique=True)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title[:MAX_LEN_TO_STR]

    class Meta:
        ordering = ('title',)
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Post(models.Model):
    """Модель постов
    Атрибуты:
        text : Текст
        pub_date : Дата публикации
        author : Автор
        image: Изображение
        group : Группа
    """

    text = models.TextField('Текст',
                            help_text='Введите текст поста')
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    image = models.ImageField(
        'Картинка',
        upload_to='posts/',
        null=True,
        blank=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='Группа',
        help_text='Группа, к которой будет отсносится пост',
    )

    def __str__(self):
        return self.text[:MAX_LEN_TO_STR]

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    """Модель комментариев
    Атрибуты:
        post : Пост
        author : Автор
        text : Текст
        created : Группа
    """

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self) -> str:
        return self.text[:MAX_LEN_TO_STR]
