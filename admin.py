from django.contrib import admin

# Register your models here.

from blog.models import BlogPost, Blogger, Comment

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_date')

@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    pass
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'post_date')

# admin.site.register(BlogPost)
# admin.site.register(Blogger)
# admin.site.register(Comment)