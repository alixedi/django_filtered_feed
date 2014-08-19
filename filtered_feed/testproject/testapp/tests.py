import feedparser

from django.test import TestCase
from django.test.client import Client

from .models import Book
from django.contrib.sites.models import Site


class FilteredFeedTest(TestCase):

    def setUp(self):
        books = [('Intro to Java', 1000), ('Intro to C', 800), ('Intro to Python', 200)]
        for name, pages in books:
            Book.objects.create(name=name, pages=pages)
        # django syndication framework uses site - it has to be localhost
        site = Site.objects.get()
        site.domain = 'http://localhost:8000'
        # make client
        self.client = Client()

    def test_basic(self):
        """
        Hits the feed - it should return all entries
        """
        res = self.client.get("http://localhost:8000/books/feed")
        self.assertEqual(200, res.status_code)
        r = feedparser.parse(res.content)
        entries = [entry['summary_detail']['value'] for entry in r['entries']]
        self.assertEqual(3, len(entries))

    def test_filter(self):
        """
        Hits the feed at pages less than 500 - should give us Python
        """
        res = self.client.get("http://localhost:8000/books/feed?pages=500")
        self.assertEqual(200, res.status_code)
        r = feedparser.parse(res.content)
        entries = [entry['summary_detail']['value'] for entry in r['entries']]
        self.assertEqual(1, len(entries))
        self.assertEqual(entries.pop(), 'Intro to Python')
