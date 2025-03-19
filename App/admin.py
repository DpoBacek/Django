from django.contrib import admin
from .models import Notification, Author, Book

admin.site.register(Notification)
admin.site.register(Author)
admin.site.register(Book)