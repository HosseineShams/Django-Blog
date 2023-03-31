from django.contrib import admin
from .models import Post, Category, Tag, Comment
from django.contrib import messages


class PostInline(admin.TabularInline):
    model = Post
    extra = 0

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

@admin.action(description='منتشر کردن پست های انتخاب شده')
def make_publish(modeladmin, request, queryset):
    updated = queryset.update(publish=True)
    messages.success(request, f"{updated}پست های انتخاب شده منتشر شدند.")

@admin.action(description='عدم نمایش کردن پست های انتخاب شده')
def make_hidden(modeladmin, request, queryset):
    updated = queryset.update(publish=False)
    messages.success(request, "پست های انتخاب شده در سایت مخفی شدند")
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'author', 'category', 'publish', 'get_date',)
    list_filter = ('publish', 'author', 'created_at')
    search_fields = ('title', 'body', 'author__username', 'author__first_name')
    list_editable = ('category', 'publish')
    list_display_links = ('author', 'title')
    list_per_page = 100
    sortable_by = ('title', 'author')
    #ordering = ('title','author')
    readonly_fields = ('slug',)
    actions = (make_publish, make_hidden)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'post', 'user', 'is_hidden', 'status')
    list_filter = ('is_hidden', 'status', 'post')
    search_fields = ('body',)

