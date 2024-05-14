from django.contrib import admin
from django.urls import path
from accounts import views


app_name='accounts'
urlpatterns = [
path('register/',views.UserRegister.as_view(), name='register' ),
path('', views.Homeview.as_view(), name='home'),
path('<int:user_id>/', views.Homeview.as_view(), name='home_user'),
path('accounts/login/',views.LoginView.as_view(), name='login'),
path('accounts/logout/',views.logoutView.as_view(), name='logout')
    
]