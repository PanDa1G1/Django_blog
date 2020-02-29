from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.index_list, name='index_list'),
    path('<slug:category>/<int:year>/<int:month>/<int:day>/<slug:post>/', views.article_details, name='article_details'),
    path('web/', views.web_list, name='web_list'),
    path('crypto/', views.crypto_list, name='crypto_list'),
    path('coding/', views.coding_list, name='coding_list'),
    path('collecting/', views.collecting_list, name='collecting_list'),
    path('penetrate/', views.penetrate_list, name='penetrate_list'),
    path('<slug:category>/tag/<slug:tag_slug>', views.post_list, name='post_list_by_tag'),
]
