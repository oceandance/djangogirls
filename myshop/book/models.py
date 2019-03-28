from django.db import models
from django.utils import timezone
from django.conf import settings


class BookCategory(models.Model):
    category_id = models.IntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=40, null=True)


class Authors(models.Model):
    author_id = models.IntegerField(primary_key=True, unique=True, default=0)
    author_name = models.CharField(max_length=40, null=True)
    biography = models.TextField()
    birthday_date = models.DateTimeField(blank=True, null=True)
    death_date = models.DateTimeField(blank=True, null=True)


class Books(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=40, null=True)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, null=False, default=0)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, null=False, default=0)
    price = models.IntegerField(default=0)
    description = models.TextField(null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Orders(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)


