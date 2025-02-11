from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post
from .forms import PostForm

def posts_list(request):
    posts = list(Post.objects.values())
    return JsonResponse(posts, safe=False)

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return JsonResponse({"title": post.title, "description": post.description, "author": post.author})

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts_list")
    else:
        form = PostForm()
    return render(request, "post/create_post.html", {"form": form})

def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("posts_list")

