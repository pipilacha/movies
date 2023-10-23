from rest_framework.routers import DefaultRouter

from .views import ActorViewSet

router = DefaultRouter()
router.register(r'actors', ActorViewSet, basename='actor')

urlpatterns = router.urls
