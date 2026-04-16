from django.urls import path, include
from blogg import views
from .views import MyFirstAPI
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('@<str:username>/', views.profile_view, name='profile'),
    path('api/test/', MyFirstAPI.as_view()),
]