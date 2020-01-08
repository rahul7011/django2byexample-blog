from django.contrib import admin
from .models import Post

# Register your models here.
#admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish',
    'status')
    list_filter = ('status', 'created', 'publish',)
    search_fields = ('title', 'body','status',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')