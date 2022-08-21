import random as r
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def index(request):
    #Tools
    latest_posts = Post.objects.all().order_by('-id')[:6]
    categories = Category.objects.all()
    try:
        adm = SiteAdmin.objects.get(pk=1)
    except:
        adm = None

    #self
    all_posts = Post.objects.all()
    featured = Post.objects.filter(featured__in=[True])
    ind = r.sample(range(1, len(categories)+1), 4)
    box1 = Post.objects.filter(category=ind[0])[0]
    box2 = Post.objects.filter(category=ind[1])[0]
    box3 = Post.objects.filter(category=ind[2])[0]
    box4 = Post.objects.filter(category=ind[3])[0]
    context = {
        "latest_posts": latest_posts,
        "all_posts": all_posts,
        "adm": adm,
        'categories': categories,
        'featured': featured,
        'box1': box1,
        'box2': box2,
        'box3': box3,
        'box4': box4,
    }
    return render(request, "people/index.html", context)


def post(request, slug):
    # Tools
    latest_posts = Post.objects.all().order_by('-id')[:6]
    categories = Category.objects.all()
    try:
        adm = SiteAdmin.objects.get(pk=1)
    except:
        adm = None
    obj = Post.objects.get(slug=slug)
    context = {
        "post": obj,
        'categories': categories,
        'latest_posts': latest_posts,
        'adm': adm,
    }
    return render(request, "people/image-post.html", context)


def categories(request, id):
    # Tools
    latest_posts = Post.objects.all().order_by('-id')[:6]
    categories = Category.objects.all()
    try:
        adm = SiteAdmin.objects.get(pk=1)
    except:
        adm = None

    # self
    post_by_category = Post.objects.filter(category=id)
    name = Category.objects.get(id=id)
    all_posts = Post.objects.all()
    p = Paginator(post_by_category, 3)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    context = {
        "post_by_category": post_by_category,
        "all_posts": all_posts,
        "name": name,
        'categories': categories,
        'page_obj': page_obj,
        'adm': adm,
        'latest_posts': latest_posts,

    }
    return render(request, "people/category.html", context)


def about(request):
    # Tools
    latest_posts = Post.objects.all().order_by('-id')[:6]
    categories = Category.objects.all()
    try:
        adm = SiteAdmin.objects.get(pk=1)
    except:
        adm = None

    context = {
        "latest_posts": latest_posts,
        'categories': categories,
        'adm': adm,
    }
    return render(request, "people/about.html", context)


def contact(request):
    # Tools
    latest_posts = Post.objects.all().order_by('-id')[:6]
    categories = Category.objects.all()
    try:
        adm = SiteAdmin.objects.get(pk=1)
    except:
        adm = None
    context = {
        "latest_posts": latest_posts,
        'categories': categories,
        'adm': adm,
    }
    return render(request, "people/contact.html", context)


def all_post(request):
    # Tools
    latest_posts = Post.objects.all().order_by('-id')[:6]
    categories = Category.objects.all()
    try:
        adm = SiteAdmin.objects.get(pk=1)
    except:
        adm = None

    # self
    all_posts = Post.objects.all()
    p = Paginator(all_posts, 10)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {
        "page_obj": page_obj,
        'categories': categories,
        "latest_posts": latest_posts,
    }
    return render(request, "people/all.html", context)
