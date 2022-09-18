from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('register/', views.register,name="register"),
    path('login/', views.login,name="login"),
    path('logout/', views.logout_user,name="logout"),
    path('delete/<int:pk>', views.delete_item,name="delete"),

    ]