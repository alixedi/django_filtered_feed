from django.conf.urls import patterns, url
from .views import BookFilteredFeed, BookDetailView

urlpatterns = patterns('',
    url(r'^books/$', BookFilteredFeed.as_view(), name='book_feed'),
    url(r'^books/(?P<pk>\d+)/$', BookDetailView.as_view(), name='book_detail'),
)