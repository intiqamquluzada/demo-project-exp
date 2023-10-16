from django.urls import path
from myapp.views import index_view

urlpatterns = [
    path("", index_view, name="index"),
]