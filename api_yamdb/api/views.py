from rest_framework import filters, mixins, permissions, viewsets

from reviews.models import Title, Comment, Review
from .serializers import (CommentSerializer, ReviewSerializer)


class TitleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Title.objects.all()
    serializer_class = Title.Serializer


class CommentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ReviewViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer