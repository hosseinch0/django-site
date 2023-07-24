from django.urls import path
from blog.views import *

app_name = "blog"

urlpatterns = [
    path("", blog_view, name="index"),
    path("<int:pid>", blog_single, name="single"),
    path("test/", test, name = "test"),
    path("author/<str:author_username>", blog_view, name = "author"),
    path("category/<str:cat_name>", blog_view, name = "category"),
    path("search/", blog_search, name = "search")
]
