from django.urls import path
from . import views
from main.views import login_page

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", login_page, name="login"),

]
