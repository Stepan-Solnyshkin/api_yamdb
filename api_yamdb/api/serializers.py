from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from reviews.models import Comment, Title, Review
from users.models import User


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment