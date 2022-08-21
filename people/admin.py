from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'category', 'created_on')
    list_filter = ("status", "created_on", 'category')
    search_fields = ['title', 'content', 'category', 'status']
    prepopulated_fields = {'slug': ('title',)}


admin.site.site_title = "The People's View Administration"
admin.site.site_header = "The People's View Administration"
admin.site.index_title = "The People's View Administration"

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(SiteAdmin)
