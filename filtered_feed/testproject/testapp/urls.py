from django.conf.urls import patterns, url
from .views import BookListView, BookDetailView, BookFilteredFeed

urlpatterns = patterns('',
    url(r'^books/$', BookListView.as_view(), name='book_list'),
    url(r'^books/(?P<pk>\d+)/$', BookDetailView.as_view(), name='book_detail'),
    url(r'^books/feed$', BookFilteredFeed.as_view(), name='book_feed'),
)