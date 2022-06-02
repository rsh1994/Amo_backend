from .models import Board
from rest_framework import serializers

class BoardSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname')
    class Meta:
        model = Board
        fields = ['id', 'title', 'created_at', 'user', 'body']