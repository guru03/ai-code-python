from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import AngularViewSet, update_angular

router = DefaultRouter()
router.register(r'ngapi', AngularViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('ngapi/update/<int:pk>/', update_angular, name='update_angular'),
    path('ngapi/update/', update_angular, name='update_angular'),
]