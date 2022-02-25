from blogger.models import Category, CategoryToPost, Post
from django.contrib import admin
from django.contrib.auth.models import User

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class CategoryToPostInline(admin.TabularInline):
    model = CategoryToPost
    extra = 1

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    exclude = ('author',)
    inlines = [CategoryToPostInline]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)