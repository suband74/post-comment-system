from rest_framework import serializers

from .models import Articles, Comments


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

    def create(self, validated_data):
        return Comments.objects.create(**validated_data)


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'

    def create(self, validated_data):
        return Articles.objects.create(**validated_data)
