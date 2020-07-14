from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import add_blog
from .forms import add_post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request):
    blogs = add_blog.objects.all()
    #blogs = list(blogs)
    page = request.GET.get('page', 1)
    paginator = Paginator(blogs, 2)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    return render(request,'index.html',{'blog':blogs})

def link(request):
    return render(request, 'link.html')

def addblog(request):
    if request.method =='POST':
        form = add_post(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = add_post()
    return render(request,'add-blog.html',{
        'form':form
    })

def detail_view(request, id): 
    context ={} 
    context["data"] = add_blog.objects.get(id = id)    
    return render(request, "detail_view.html", context) 

def update_view(request, id):  
    context ={} 
    obj = get_object_or_404(add_blog, id = id) 
    form = add_post(request.POST or None, instance = obj) 

    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/"+id) 
   
    context["form"] = form 
  
    return render(request, "update_view.html", context) 