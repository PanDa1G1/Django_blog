from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Articles, Category
from taggit.models import Tag
import markdown
# Create your views here.


def index_list(request):

    categories = Category.objects.all()
    result = [i for i in categories if i.id == i.parent.id]
    print(result)
    return render(request, "blog/post/index.html", {"categories": result})


def web_list(request):

    childList = Category.objects.filter(parent_id=1)
    childList = [i for i in childList if i.blog_category.all()]
    return render(request, "blog/post/article_list.html", {"childList": childList})

def crypto_list(request):

    childList = Category.objects.filter(parent_id=5)
    childList = [i for i in childList if i.blog_category.all()]
    return render(request, "blog/post/article_list.html", {"childList": childList})


def coding_list(request):

    childList = Category.objects.filter(parent_id=4)
    childList = [i for i in childList if i.blog_category.all()]
    return render(request, "blog/post/article_list.html", {"childList": childList})


def collecting_list(request):

    childList = Category.objects.filter(parent_id=6)
    childList = [i for i in childList if i.blog_category.all()]
    return render(request, "blog/post/article_list.html", {"childList": childList})


def penetrate_list(request):

    childList = Category.objects.filter(parent_id=7)
    childList = [i for i in childList if i.blog_category.all()]
    return render(request, "blog/post/article_list.html", {"childList": childList})


def article_details(request, category,year, month, day, post):

    posts = get_object_or_404(Articles, slug=post)
    id = Category.objects.get(slug=category).parent_id
    parent = Category.objects.get(id=id)
    childList = Category.objects.filter(parent_id=id)
    childList = [i for i in childList if i.blog_category.all()]
    md = markdown.Markdown(
        extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        ]
    )
    body = posts.body
    md.convert(body)
    #print(md.toc)
    return render(request,"blog/post/article_details.html", {"post": posts, "childList": childList, 'category': parent, "toc": md.toc})

def post_list(request, category,tag_slug=None):
    posts = Articles.objects.all()
    tag_ = None
    if category:
        tag_ = Category.objects.get(slug=category)
        id = tag_.parent_id
        childList = Category.objects.filter(parent_id=id)
        childList = [i for i in childList if i.blog_category.all()]
    if tag_slug:
        tag_ = Tag.objects.get(slug=tag_slug)
        posts = posts.filter(tags__in=[tag_])
        #print(posts, tag_, sep="\n")
    return render(request, 'blog/post/tag_list.html', {"childList": childList,  "posts": posts})


