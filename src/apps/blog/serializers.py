from rest_framework import serializers

from .models import Comment, Posts


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

    def create(self, validated_data):
        return Posts.objects.create(**validated_data)
