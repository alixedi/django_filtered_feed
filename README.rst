=============================
django_filtered_feed
=============================

.. image:: https://badge.fury.io/py/django_filtered_feed.png
    :target: http://badge.fury.io/py/django_filtered_feed
    
.. image:: https://travis-ci.org/alixedi/django_filtered_feed.png?branch=master
        :target: https://travis-ci.org/alixedi/django_filtered_feed

.. image:: https://pypip.in/d/django_filtered_feed/badge.png
        :target: https://crate.io/packages/django_filtered_feed?version=latest

.. image:: https://coveralls.io/repos/alixedi/django_filtered_feed/badge.png
  :target: https://coveralls.io/r/alixedi/django_filtered_feed


So the average-joe RSS is binary ie either you subscribe to a feed or you don't. This approach results in a ridiculous amount of junk in our inbox. What if we could subscribe ``define`` the feed that we would like to subscribe to? Thanks to the stellar `django syndication framework <https://docs.djangoproject.com/en/dev/ref/contrib/syndication/>`_ and `django filters <https://github.com/alex/django-filter>`_, I was able to hack together a fix.


If you have a ``Book`` model like so: ::

    class Book(models.Model):
        name = models.CharField(max_length=256)
        pages = models.IntegerField()

    def __unicode__(self):
        return self.name

A `django_filter <https://github.com/alex/django-filter>`_ ``FilterSet`` like so: ::

    class BookFilterSet(django_filters.FilterSet):
        pages = django_filters.NumberFilter(lookup_type='lt')
        class Meta:
            model = Book
            fields = ['pages']

A ``FilteredFeed`` class like so: ::

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

And finally, if we have the following 3 books in our DB:

1. Introduction to Python (100 pages)
2. Introduction to C (300 pages)
3. Javascript - The good parts (300 pages)

Hitting `http://localhost:8000/books/feed <http://localhost:8000/books/feed>`_ will give you an RSS feed includes:

* Introduction to Python
* Introduction to C
* Javascript - The good parts

And hitting `http://localhost:8000/books/feed?pages=200 <http://localhost:8000/books/feed?pages=200>`_ will give you an RSS feed that just includes:

* Introduction to Python

You users will forever remain grateful for sparing them the deluge that follows a binary subscription. You will be hailed the king of syndication, worshipped as a rock star and live happily ever after. The best part is that it takes a minute to get started: ::

    pip install django_filtered_feed

Followed ofcourse by including `filtered_feed` in your `INSTALLED_APPS`. ::

    INSTALLED_APPS = (
        ...
        'filtered_feed',
        ...
    )