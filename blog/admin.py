import imp
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'data_created', 'author')

# Register your models here.
admin.site.register(Post, PostAdmin)
