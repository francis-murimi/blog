from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('register/',views.user_register, name='user_register'),
    path('login/',views.log_in,name='log_in'),
    path('logout/',views.log_out,name='log_out'),
]