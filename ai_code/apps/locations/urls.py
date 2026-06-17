from django.urls import path
from . import views

urlpatterns = [
    path("cities/<int:state_id>/", views.cities_by_state, name="cities_by_state"),
]
