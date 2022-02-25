from django.urls import path
from . import views

app_name = 'blogger'

urlpatterns = [
    path('blog/<slug>/',views.getPost, name='getPost'),
    path('blogs/',views.getList,name='getList' ),
    
]
