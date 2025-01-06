from django.urls import path, include
from . import views

app_name = 'users'
# from users import views

urlpatterns = [
    path('register/', views.register_view, name="register"),
]