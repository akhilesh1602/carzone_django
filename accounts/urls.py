from django.urls import path
from accounts import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('logoutt', views.logoutt, name="logout"),
    path('registerr', views.registerr, name="register"),

]
