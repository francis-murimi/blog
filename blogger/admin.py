from blogger.models import Category, CategoryToPost, Post,Solutions,Comment
from django.contrib import admin
from django.contrib.auth.models import User

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class CategoryToPostInline(admin.TabularInline):
    model = CategoryToPost
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','status','pub_date', 'updated']
    list_filter = ['status','pub_date', 'updated']
    list_editable = ['status',]
    prepopulated_fields = {"slug": ("title",)}
    exclude = ('author',)
    inlines = [CategoryToPostInline]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

class SolutionsAdmin(admin.ModelAdmin):
    model = Solutions
    #exclude = ['text','image_url','action_form']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','post']
    list_filter = ['post']
    
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Solutions,SolutionsAdmin)
admin.site.register(Comment,CommentAdmin)