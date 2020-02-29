from django import template
from ..models import Articles, Category
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.simple_tag
def total_posts():
    return Articles.objects.count()

@register.inclusion_tag('blog/post/latest_post.html')
def latestArticle():

    latest_num = 3
    arts = Articles.objects.all().order_by("-publish")[:latest_num]
    return {'latests': arts}

@register.inclusion_tag('blog/post/most_comments.html')
def most_comments():
    most_count = 3
    articleList = Articles.objects.all()
    sortedList = sorted([(i, i.comments.all().count()) for i in articleList],key=lambda key: key[1],reverse=True)[:3]
    resultList = [i[0] for i in sortedList]
    return {'mostList': resultList}

@register.filter(name="markdown")
def markdown_deal(text):
    return mark_safe(markdown.markdown(text,extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ]))


@register.inclusion_tag('blog/post/url_jump.html')
def url_jump(art,name):
    url = "{}/".format(art.slug[:-5])
    return {'src': url,"name": name}

@register.simple_tag
def get_category(category_id):
    cate = Category.objects.get(id=category_id)
    return cate.sulg

@register.inclusion_tag('blog/post/article_url.html')
def get_url(post,request):

    slug = Category.objects.get(id=post.category_id)
    src = "../../{}/{}/{}/{}/{}/".format(slug.slug,post.publish.year,post.publish.month,post.publish.day,post.slug)
    print(request.path)
    return {"posts": post, "src": src}


