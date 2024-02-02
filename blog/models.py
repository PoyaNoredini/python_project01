from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def get_absolute_urls(self):
        return reverse('blog:PostDetails', args=[self.slug, self.id])

    def __str__(self):
        return f"{self.title}"

    # return self.title

    # the save to changes in the database you must use the command """make migrations"""
    # And to apply and implement the changes, I use the """migrate""" command
    #  create superuser command


class Account(models.Model):
    GENDER_CHOICES = [
        ("woman", "Woman"),
        ("man", "Man"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account', null=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='woman')
    address = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, )
    updated = models.DateTimeField(auto_now=True, )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    #   return self.user.first_name + " " + self.user.last_name
