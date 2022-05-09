from rest_framework import filters, mixins, permissions, viewsets

from reviews.models import Title, Comment, Review
from .serializers import (CommentSerializer, ReviewSerializer)


class TitleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Title.objects.all()
    serializer_class = Title.Serializer
