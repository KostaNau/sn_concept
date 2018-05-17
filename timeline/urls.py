from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('messages', views.MessageViewSet)
router.register('feeds', views.FeedViewSet)

urlpatterns = []

urlpatterns += router.urls
