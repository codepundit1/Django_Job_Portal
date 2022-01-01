from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("admin_login/", views.admin_login, name='admin_login'),
    path("user_login/", views.user_login, name='user_login'),
    path("recruiter_login/", views.recruiter_login, name='recruiter_login'),
]
