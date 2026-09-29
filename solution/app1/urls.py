from django.urls import path

from . import views

urlpatterns = [
    path("", views.first_page),
    path("users/",views.all_users),

]