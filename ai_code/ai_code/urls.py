"""
URL configuration for ai_code project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from apps.coding.views import CodingViewSet
from apps.angular.views import AngularViewSet
from apps.javascript.views import JavascriptViewSet
from apps.locations.views import CityViewSet, StateViewSet


router = DefaultRouter()
router.register(r"angular", AngularViewSet, basename="angular")
router.register(r"coding", CodingViewSet, basename="coding")
router.register(r"javascript", JavascriptViewSet, basename="javascript")
router.register(r"states", StateViewSet, basename="states")   # 👈 new
router.register(r"cities", CityViewSet, basename="cities")    # 👈 new

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
]
