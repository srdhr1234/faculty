from django.contrib import admin
from django.contrib.auth.models import User
from .models import Publication_C, Publication_J, BookChapter, Book, Patent, Copyright

# Register your models here.
admin.site.register(Publication_C)
admin.site.register(Publication_J)
admin.site.register(BookChapter)
admin.site.register(Book)
admin.site.register(Patent)
admin.site.register(Copyright)
