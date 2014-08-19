=============================
django_filtered_feed
=============================

.. image:: https://badge.fury.io/py/django_filtered_feed.png
    :target: http://badge.fury.io/py/django_filtered_feed
    
.. image:: https://travis-ci.org/alixedi/django_filtered_feed.png?branch=master
        :target: https://travis-ci.org/alixedi/django_filtered_feed

.. image:: https://pypip.in/d/django_filtered_feed/badge.png
        :target: https://crate.io/packages/django_filtered_feed?version=latest


If you have a `Book` model like so: ::

    class Book(models.Model):
        name = models.CharField(max_length=256)
        pages = models.IntegerField()

    def __unicode__(self):
        return self.name

A [django_filter](https://github.com/alex/django-filter) `FilterSet` like so: ::

    class BookFilterSet(django_filters.FilterSet):
        pages = django_filters.NumberFilter(lookup_type='lt')
        class Meta:
            model = Book
            fields = ['pages']

A `FilteredFeed` class like so: ::

    class BookFilteredFeed(BaseFilteredFeed):
        model = Book
        filter_set = BookFilterSet
        title = "BookFeed"
        link = "http://localhost:8000"
        description = "Get alerts for new books - less than given number of pages!"

        def item_link(self, item):
            return reverse('book_detail', args=[item.id])

Hook up the necessary urls like so: ::

    urlpatterns = patterns('',
        url(r'^books/feed$', BookFilteredFeed.as_view(), name='book_feed'),
    )

And finally, 3 books, like so: ::

    1. Introduction to Python (100 pages)
    2. Introduction to C (300 pages)
    3. Javascript - The good parts (300 pages)

Hitting `http://localhost:8000/books/feed` will give you an RSS feed that looks like: ::

    Introduction to Python
    Introduction to C
    Javascript - The good parts

And hitting `http://localhost:8000/books/feed?pages=200` will give you an RSS feed that looks like: ::

    Introduction to Python

You users will forever remain grateful for sparing them the deluge that follows a binary subscription. You will be hailed the king of syndication, worshipped as a rock star and live happily ever after.

The best part is that it takes a minute to get started: ::

    pip install django_filtered_feed

Followed ofcourse by including `filtered_feed` in your `INSTALLED_APPS`. ::


Features
--------

* TODO