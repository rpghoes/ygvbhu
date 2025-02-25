from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Post
from .forms import PostForm

# Страница логина
def login_page(request):
    return render(request, 'login.html')

# Аутентификация пользователя
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('posts')
    return redirect('login')

# Выход пользователя
def logout_user(request):
    logout(request)
    return redirect('login')

# Все посты
def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

# Посты текущего пользователя
@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'posts.html', {'posts': posts})

# Детальная страница поста
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_detail.html', {'post': post})

# Создание поста
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

# Удаление поста
@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user == post.author or request.user.is_superuser:
        post.delete()
        return redirect('posts')
    return HttpResponseForbidden("Недостаточно прав")
