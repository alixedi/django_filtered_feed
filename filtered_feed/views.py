from django.views.generic import ListView
from django.contrib.syndication.views import Feed
from django.utils import feedgenerator

from .viewmixins import ListFilteredMixin


_FEED_FORMATS = {
    'atom1': feedgenerator.Atom1Feed,
    'rss0.91': feedgenerator.RssUserland091Feed,
    'rss2.0': feedgenerator.Rss201rev2Feed,
}


class ListFilteredView(ListFilteredMixin, ListView):
    pass


class BaseFilteredFeed(ListFilteredView, Feed):
    """
    Bridge to let Django syndication feeds operate like a normal class-based-view.
    This introduces the ``as_view()`` method, attributes like ``self.request`` and allows to assign attributes to 'self'.
    """
    format = 'rss2.0'

    def __init__(self, **kwargs):
        ListFilteredView.__init__(self, **kwargs)

        # Allow this view to easily switch between feed formats.
        format = kwargs.get('format', self.format)
        try:
            self.feed_type = _FEED_FORMATS[format]
        except KeyError:
            raise ValueError("Unsupported feed format: {0}. Supported are: {1}".format(
                self.format, ', '.join(sorted(_FEED_FORMATS.iterkeys()))
            ))

    def get(self, request, *args, **kwargs):
        # Pass flow to the original Feed.__call__
        return self.__call__(request, *args, **kwargs)

    def items(self, obj):
        return self.get_queryset()
