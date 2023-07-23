from django import template
from blog.models import Post, Category
register = template.Library()


@register.simple_tag(name='post_count')
def func():
    post = Post.objects.filter(status=1).count()
    return post


@register.simple_tag(name='posts')
def function():
    posts = posts.objects.filter(status=1)
    return posts


@register.filter
def snippet(var, args):
    return var[:args]


@register.inclusion_tag('blog/popularposts.html')
def latest_posts(arg=2):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/post-categories.html')
def postCategories():
    posts = Post.objects.filter(status=1)
    Categories = Category.objects.all()
    category_dict = {}
    for name in Categories:
        category_dict[name] = posts.filter(category=name).count()
    return {'categories': category_dict}
