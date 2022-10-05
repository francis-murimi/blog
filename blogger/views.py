from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render,redirect
from blogger.models import CategoryToPost, Post, Category,Solutions, Comment
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.views.generic.list import ListView
from django.views.generic import ListView
from .forms import CommentForm

def homePage(request):
    blogs = Post.objects.filter(status= 1)[:3]
    products = Solutions.objects.all()
    context = {'blogs':blogs,
                'products':products}
    template = loader.get_template('blogger/home.html')
    return HttpResponse(template.render(context,request))

class PostList(ListView):
    model = Post
    template_name = 'blogger/list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'blogs'  # Default: object_list
    paginate_by = 4 # Number of posts per page
    queryset = Post.objects.filter(status= 1)  # Default: Model.objects.all()


def getPost(request, slug):
    # Get specified post
    post = Post.objects.get(slug=slug)
    categories = CategoryToPost.objects.filter(post=post)
    #comments
    comments = Comment.objects.filter(post= post)
    new_comment = None
    # Comment posted
    if request.method == 'POST': 
        form = CommentForm(data=request.POST)
        if form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            new_comment.name = request.user
            # Save the comment to the database
            new_comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    context = {'post':post, 'form':form, 'comments':comments,'categories':categories}
    template = loader.get_template('blogger/detail.html')
    return HttpResponse(template.render(context,request))

class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.all()
    paginate_by = 5
    context_object_name = 'category_list'
    template_name = 'blogger/category_list.html'

def getCategory(request, categorySlug,):
    category = Category.objects.get(slug = categorySlug)
    posts = Post.objects.filter(categories=category).order_by('-pub_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 4) # Number of posts per page
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    template = loader.get_template('blogger/category.html')
    context = {'category':category,'posts':posts}
    return HttpResponse(template.render(context,request))

