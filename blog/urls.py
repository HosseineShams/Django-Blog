from django.urls import path
from . import views 

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blog/new/', views.add_blog, name='add-blog'),
    path('blog/<str:slug>/', views.blog_details, name='details'),
    path("search/", views.search, name="search"),
    
]
