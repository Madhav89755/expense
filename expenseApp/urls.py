from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('register/', views.register,name="register"),
    path('username-check/', views.username_check,name="username_check"),
    path('login/', views.login,name="login"),
    path('logout/', views.logout_user,name="logout"),
    path('delete/', views.delete_item,name="delete"),
    path('update/', views.update_item,name="update"),
    path('summary/', views.summary,name="summary_expense"),

    ]