from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list_view, name='blog_list'),
    path('<int:id>/', views.blog_detail_view, name='blog_detail'),
    path('create/', views.blog_create_view, name='blog_create'),
    path('update/<int:id>/', views.blog_update_view, name='blog_update'),
    path('delete/<int:id>/', views.blog_delete_view, name='blog_delete'),
]
