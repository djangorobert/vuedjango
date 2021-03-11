from django.contrib import admin

# Register your models here.
from .models import Article
from  .models import Author

admin.site.register(Article)
admin.site.register(Author)

