from django.contrib import admin
from .models import Blog
from tinymce.widgets import TinyMCE
from django.db import models


class BlogAdmin(admin.ModelAdmin):
    fieldsets=[
        ("Title", {"fields" : ["Title"]}),
        ("Content", {"fields" : ["Content"]}),
        ("Date", {"fields": ["Published"]}),
         ]

    formfield_overrides = {
        models.TextField : {
            'widget' : TinyMCE()}}

admin.site.register(Blog, BlogAdmin)
