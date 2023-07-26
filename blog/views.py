from django.shortcuts import render, get_list_or_404
from django.http import HttpRequest, JsonResponse
from blog.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.decorators import login_required
# Create your views here.

# @login_required
def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get("author_username"):
        posts = posts.filter(author__username= kwargs['author_username'])
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts.get_page(1)
    except EmptyPage:
        posts.get_page(1)
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

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == "GET":
        if s := request.GET.get("s"):
            posts = posts.filter(content__contains=s)
            # posts = Paginator(posts,3)
        # try:
        #     page_number = request.GET.get('page')
        #     posts = posts.get_page(page_number)
        # except PageNotAnInteger:
        #     posts.get_page(1)
        # except EmptyPage:
        #     posts.get_page(1)
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)