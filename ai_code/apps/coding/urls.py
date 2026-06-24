from django.urls import include, path
from rest_framework.routers import DefaultRouter

from views import CodingViewSet

router = DefaultRouter()
router.register(r"coding", CodingViewSet, basename="coding")


urlpatterns = [
    path("", include(router.urls)),  # all CRUD endpoints come from here
]
