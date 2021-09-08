from django.shortcuts import render
from blog.models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, ListView
from django.db.models import Q

# Create your views here.


def home(request):
    cats = Category.objects.all()

    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 2)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    data = {
        'posts': posts,
        'cats': cats
    }
    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cat = post.cat
    related_posts = Post.objects.filter(cat=cat)[:10]
    return render(request, 'posts.html', {'post': post, 'cat': cat, 'related_posts': related_posts})


def category(request, url):
    cats = Category.objects.all()
    cat = Category.objects.get(url=url)

    posts_list = Post.objects.filter(cat=cat)
    paginator = Paginator(posts_list, 2)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "category.html", {'cat': cat, 'posts': posts, 'cats': cats})


def SearchResultsView(request):
    query = request.GET.get('q')
    object_list = Post.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    )
    return render(request, 'search_results.html', {'object_list': object_list, 'query': query})
