from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from posts.models import Group, Post

from .permissions import AuthorOrReadOnly
from .serializers import (CommentSerializer,
                          GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    """ВьюСет для Постов."""

    queryset = Post.objects.select_related('group', 'author').all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, AuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ВьюСет для Групп."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """ВьюСет для Комментариев."""

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, AuthorOrReadOnly]

    def get_queryset(self):
        post = get_object_or_404(
            Post.objects.select_related('group', 'author'),
            id=self.kwargs.get('post_id')
        )
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(
            Post.objects.select_related('group', 'author'),
            id=self.kwargs.get('post_id')
        )
        serializer.save(author=self.request.user, post=post)
