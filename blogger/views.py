from django.template import loader
from blogger.models import Post, Category
from django.http import HttpResponse, Http404,HttpResponseRedirect

def getList(request):
    blogs = Post.objects.all()
    context = {'blogs':blogs}
    template = loader.get_template('blogger/list.html')
    return HttpResponse(template.render(context,request))

def getPost(request, slug):
    # Get specified post
    post = Post.objects.get(slug=slug)
    context = {'post':post,}
    template = loader.get_template('blogger/detail.html')
    return HttpResponse(template.render(context,request))
