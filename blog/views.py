from django.shortcuts import render, get_list_or_404
from django.http import HttpRequest, JsonResponse
from blog.models import Post
# Create your views here.


def blog_view(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)


def blog_single(request, pid):
    posts = get_list_or_404(Post, pk=pid)
    context = {"posts": posts}
    return render(request, "blog/blog-single.html", context)


def test(request, pid):
    posts = get_list_or_404(Post, pk=pid)
    context = {"posts": posts}
    return render(request, "test.html", context)
