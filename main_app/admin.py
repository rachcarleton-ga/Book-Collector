from django.contrib import admin

from .models import Book, Reading, Bookmark, Photo
# Register your models here.

admin.site.register(Book)
admin.site.register(Reading)
admin.site.register(Bookmark)
admin.site.register(Photo)