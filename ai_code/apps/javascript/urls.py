from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import JavascriptViewSet, update_javascript

router = DefaultRouter()
router.register(r"javascript", JavascriptViewSet, basename="javascript")


urlpatterns = [
    path("", include(router.urls)),  # all CRUD endpoints come from here
]
