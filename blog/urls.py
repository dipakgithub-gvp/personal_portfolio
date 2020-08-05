from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_index, name="blog_index"),
    path('<int:blog_id>',views.blog_post, name='blog_post'),
]