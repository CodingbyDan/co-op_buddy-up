from django.urls import path, include
from . import views

app_name = 'posts'
# from users import views

urlpatterns = [
    path('', views.posts_list, name="list"),
    path('<slug:slug>', views.post_page, name="page"),
]