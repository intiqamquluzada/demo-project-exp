from django.urls import path
from myapp.views import index_view, detail_view, car_view

urlpatterns = [
    path("", index_view, name="index"),
    path("detail/<int:id>/", detail_view, name='detail'),
    path("car/", car_view, name='car'),
]