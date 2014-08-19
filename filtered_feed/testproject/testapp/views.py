from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse

import django_filters
from filtered_feed.views import BaseFilteredFeed
from filtered_feed.viewmixins import ListFilteredMixin

from .models import Book


class BookFilterSet(django_filters.FilterSet):
    pages = django_filters.NumberFilter(lookup_type='lt')
    class Meta:
        model = Book
        fields = ['pages']


class BookListView(ListFilteredMixin, ListView):
    model = Book
    filter_set = BookFilterSet


class BookDetailView(DetailView):
    model = Book


class BookFilteredFeed(BaseFilteredFeed):
    model = Book
    filter_set = BookFilterSet
    title = "BookFeed"
    link = "http://localhost:8000"
    description = "Get alerts for new books - less than given number of pages!"

    def item_link(self, item):
        return reverse('book_detail', args=[item.id])

