from .models import Board, Comment
from rest_framework import serializers

class BoardSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname')
    class Meta:
        model = Board
        fields = ['id', 'title', 'created_at', 'user', 'body']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname')
    class Meta:
        model = Comment
        fields = ['id', 'blog', 'user', 'created_at', 'comment']