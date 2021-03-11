from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=64)
    author = models.ForeignKey('vue_app.Author', on_delete=models.CASCADE)
    content = models.TextField()
    slug = models.CharField(default='', max_length=64)
    timestamp = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=64)
    slug = models.CharField(default='', max_length=64)

    def __str__(self):
        return self.name