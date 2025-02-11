from django.urls import path
from .views import posts_list, post_detail, create_post, delete_post

urlpatterns = [
    path('posts/', posts_list, name="posts_list"),  # Список всех постов
    path('posts/<int:id>/', post_detail, name="post_detail"),  # Просмотр одного поста
    path('posts/new/', create_post, name="create_post"),  # Создание нового поста
    path('posts/<int:id>/delete/', delete_post, name="delete_post"),  # Удаление поста
]
