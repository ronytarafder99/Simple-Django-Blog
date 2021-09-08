from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home,post,category,SearchResultsView


urlpatterns = [
    path('', home),
    path('home/',home),
    path('blog/<slug:url>',post),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('category/<slug:url>',category)
]