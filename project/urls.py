from . import views
from django.urls import path
from .views import profile_upload


urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.profile_upload, name="profile_upload"),
]