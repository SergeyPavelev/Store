from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AddressViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'addresses', AddressViewSet, basename='addresses')

urlpatterns = router.urls
