from django.urls import path 
from user_app import views

urlpatterns = [
    path("register/",views.register,name='register'),
    
]
