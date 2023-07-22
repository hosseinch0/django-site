from django.contrib import admin
from blog.models import Post,Category
# Register your models here.

# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "EMPTY"
    list_display = ('titles', 'author', 'counted_view', 'status', 'created_date', 'published_date', 'updated_date')
    list_filter = ('status', 'author')
    search_fields = ('titles',)



admin.site.register(Category)
admin.site.register(Post,PostAdmin)




