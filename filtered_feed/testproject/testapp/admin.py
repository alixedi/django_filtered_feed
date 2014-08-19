from django.contrib import admin
from testapp.models import Book

class BookAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)