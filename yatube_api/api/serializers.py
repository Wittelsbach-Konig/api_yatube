from rest_framework import serializers

from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели постов."""

    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели групп."""

    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class CommentSerializer(serializers.ModelSerialzer):
    """Сериалайзер для модели комментариев."""

    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = ('author', 'post', 'text', 'created')
        model = Comment
        read_only_fields = ('post',)
