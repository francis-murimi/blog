from django.template import loader
from blogger.models import Post, Category
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.views.generic.list import ListView
from django.views.generic import ListView

def homePage(request):
    blogs = Post.objects.all()
    context = {'blogs':blogs}
    template = loader.get_template('blogger/home.html')
    return HttpResponse(template.render(context,request))

class PostList(ListView):
    model = Post
    template_name = 'blogger/list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'blogs'  # Default: object_list
    paginate_by = 4 # Number of posts per page
    queryset = Post.objects.all()  # Default: Model.objects.all()

"""
def getList(request):
    blogs = Post.objects.all()
    context = {'blogs':blogs}
    template = loader.get_template('blogger/list.html')
    return HttpResponse(template.render(context,request))
    """

def getPost(request, slug):
    # Get specified post
    post = Post.objects.get(slug=slug)
    context = {'post':post,}
    template = loader.get_template('blogger/detail.html')
    return HttpResponse(template.render(context,request))

class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category_list'
    template_name = 'blogger/category_list.html'

def getCategory(request, categorySlug,):
    category = Category.objects.get(slug = categorySlug)
    posts = Post.objects.filter(categories=category).order_by('-pub_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 2) # Number of posts per page
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    template = loader.get_template('blogger/category.html')
    context = {'category':category,'posts':posts}
    return HttpResponse(template.render(context,request))

