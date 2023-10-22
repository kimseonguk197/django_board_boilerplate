from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # admin으로 들어오는 url 빼고는 아래 path로 redirect
    path('', include('board_main.urls')),
]
