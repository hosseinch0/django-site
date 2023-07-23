from django.shortcuts import render, get_list_or_404
from django.http import HttpRequest, JsonResponse
from blog.models import Post
# Create your views here.


def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)


def blog_single(request, pid):
    post = get_list_or_404(Post, pk=pid, status=1)
    context = {"posts": post}
    return render(request, "blog/blog-single.html", context)


def test(request):
    posts = get_list_or_404(Post)
    context = {"posts": posts}
    return render(request, "test.html", context)


def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)

