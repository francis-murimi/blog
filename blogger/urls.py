from django.urls import path
from .views import CategoryListView,PostList
from blogger.models import Category
from . import views
from django.views.generic import ListView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap

app_name = 'blogger'
sitemaps = {
    'blog':PostSitemap
}
urlpatterns = [
    path('',views.homePage, name='homePage'),
    path('blog/<slug>/',views.getPost, name='getPost'),
    #path('blogs/',views.getList,name='getList' ),
    path('blogs/',views.PostList.as_view(), name= 'PostList'),
    # Categories
    path('categories/', ListView.as_view(model=Category,)),
    path('categories/<categorySlug>/',views.getCategory,name='getCategory'),
    path('categories/<categorySlug>/<selected_page>/',views.getCategory, name='getCategory'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
