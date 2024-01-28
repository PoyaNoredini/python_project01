from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),  # If we want to make a comparison, we use the first one,
        # and wherever we want to display a value to the user, we use the second one.
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)  # char fild for the string character
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    # It is used to create links and follows important link rules and is used for posts and so on
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    # It shows which user this post title is being created. Each post is created by a user. The meaning of
    # ""on_deleted"" is the post as long as the user is on, and when it is off, all the posts related to this user
    # will be deleted. The meaning of ""related_name"" shows us what posts each user has.
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)  # When the post is published, we set the default time now
    created = models.DateTimeField(auto_now_add=True)
    # It shows the time when the post was created, and it may not  be published at the same moment.
    updated = models.DateTimeField(auto_now=True)  # It shows the time when the post was change and update
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)
        # It lists the posts according to the timing from the last to the first

    def get_absolute_urls(self):  # This function creates a unique urls for each post
        return reverse('blog:PostDetails', args=[self.slug, self.id])

    def __str__(self):
        return self.title


# the save to changes in the database you must use the command """make migrations"""
# And to apply and implement the changes, I use the """migrate""" command
#  create superuser command

class Account(models.Model):
    GENDER_CHOICES = (
        ('woman', 'Woman'),
        ('man', 'Man'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account', null=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='woman')
    address = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True,)
    updated = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
