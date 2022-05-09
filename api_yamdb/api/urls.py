from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import CommentViewSet, ReviewViewSet, TitleViewSet

router = SimpleRouter()
router.register('titles', TitleViewSet)
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