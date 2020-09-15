from django.contrib import admin

# Register your models here.
from api2.models import Book,Author,AuthorDetail,Press
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(AuthorDetail)
admin.site.register(Press)
