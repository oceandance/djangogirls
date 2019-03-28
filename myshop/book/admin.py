from django.contrib import admin
from .models import Books, BookCategory, Authors, Orders

admin.site.register(Books)
admin.site.register(BookCategory)
admin.site.register(Authors)
admin.site.register(Orders)
