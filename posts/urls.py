from django.urls import path, include
from . import views
# from users import views

urlpatterns = [
    path('', views.posts_list),
]