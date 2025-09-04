from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('list/', views.tweet_list, name="list"),
    path('store/', views.tweet_create, name="store"),
    path('edit/<int:tweet_id>', views.tweet_edit, name="edit"),
    path('delete/<int:tweet_id>', views.tweet_delete, name="delete"),
    path('register/', views.register, name="register"),
]
