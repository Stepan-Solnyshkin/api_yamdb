from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import (CategoryViewSet, CommentViewSet,
                       GenreViewSet, TitleViewSet, ReviewViewSet)

router = SimpleRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('genries', GenreViewSet, basename='genries')
router.register('titles', TitleViewSet, basename='titles')
router.register(
    r'^titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='review')
router.register(
    r'^titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='review')

urlpatterns = [
    path('v1/', include(router.urls)),
]
