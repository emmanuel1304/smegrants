from django.urls import path
from . import views


app_name = 'smeapp'

urlpatterns = [ 
    path('', views.home, name='home'),
    path('application/', views.application, name='application'),
    path('register/', views.register, name='register'),
    path('login/', views.login_request, name="login"),
    path('logout/', views.logout_request, name='logout'),
]
