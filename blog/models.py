from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Blog(models.Model):
    category = models.ManyToManyField(Category, related_name='category')
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to='blog/static/images/')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
