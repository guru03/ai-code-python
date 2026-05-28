from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import AngularViewSet, update_angular

router = DefaultRouter()
router.register(r"angular", AngularViewSet, basename="angular")


urlpatterns = [
    path("", include(router.urls)),  # all CRUD endpoints come from here
]
