from django.conf.urls import url
from django.urls import path
from Tea_App import views

app_name = 'Tea_App'

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('blog-details/<int:pk>/', views.blog_details, name="blog_details"),
    path('blog/', views.blog, name="blog"),
    # path('help/', views.c, name="help"),
    path('tea_details/<int:id>/', views.tea_details, name="tea_details"),
    path('types/', views.types, name="types"),
    path('help', views.Contact.as_view(), name='help'),
    path('search/',views.search,name='search'),
]
