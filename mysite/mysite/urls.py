from django.contrib import admin
from django.urls import path
from vue_app.views import frontend
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', frontend, name='frontend'),
    path('article/<slug:slug>/', frontend),
    path('author/<slug:slug>/', frontend),  # This line is new
]