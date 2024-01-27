from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('API', views.API, name='API'),
    path('api', views.api, name='api'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile/<str:pk>',views.profile,name='profile'),
]
