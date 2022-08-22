from django.urls import path, include
from .views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path("__reload__/", include("django_browser_reload.urls")),
]