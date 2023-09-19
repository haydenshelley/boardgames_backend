from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("boardgames/", include("boardgames.urls")),
    path("admin/", admin.site.urls),
]