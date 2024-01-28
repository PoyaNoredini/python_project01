from django.contrib import admin
from .models import Post, Account


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'publish')
    # In the list section, it shows us the titles we want
    list_filter = ('status', 'publish', 'created', 'author')  # filter based on list
    search_fields = ('title', 'body')
    # It searches based on the title and the text written in the body part
    prepopulated_fields = {'slug': ('title',)}
    # In order for the slug to be designed based on a general rule,
    # we use this section and whatever we give it creates a slug based on that,
    # so to speak, we designed a dictionary for the slug.
    raw_id_fields = ('author',)  # To search users and shows users based on ID
    date_hierarchy = 'publish'  # It is used to show the date, and it allows us to divide things based on time
    ordering = ('status', 'publish')  # Sorts first based on status and then published
    list_editable = ('status', 'author')
    # This option allows us to edit information without entering each post
    list_display_links = ('slug', 'publish', 'title')
    # This function converts the name into a link that directs us to the home page of creating a post


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('phone_number',)
