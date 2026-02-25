from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('follow/<str:username>/', views.follow_toggle, name='follow_toggle'),
    path('like/<int:id>/', views.like_post, name='like_post'),
    path('comment/<int:id>/', views.add_comment, name='add_comment'),
    path('create/', views.create_post, name='create_post'),
]