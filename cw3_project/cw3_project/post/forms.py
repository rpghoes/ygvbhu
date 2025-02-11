# forms.py в вашем приложении
from django import forms
from .models import Thread, Post

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['name', 'description']  # Здесь укажите поля модели, которые хотите редактировать

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'author', 'thread']  # Здесь укажите поля модели, которые хотите редактировать
