from django.urls import path
from .views import CategoryListView
from blogger.models import Category
from . import views
from django.views.generic import ListView

app_name = 'blogger'

urlpatterns = [
    path('',views.HomePage.as_view(), name='HomePage'),
    path('blog/<slug>/',views.getPost, name='getPost'),
    path('blogs/',views.getList,name='getList' ),
    # Categories
    path('categories/', ListView.as_view(model=Category,)),
    path('categories/<categorySlug>/',views.getCategory,name='getCategory'),
    path('categories/<categorySlug>/<selected_page>/',views.getCategory, name='getCategory'),
]
