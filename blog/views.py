from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.views.generic import ListView

#start from here!

def post_list(request):
    posts = Post.published.all()
    object_list = Post.published.all()
    #adding pagination
    paginator = Paginator(object_list, 2) # 3 posts in each page
    page = request.GET.get('page')      #"Get the value of a GET variable with name 'page', and if it doesn't exist, return 1". 
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
    # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    #end for adding pagination
    return render(request,'blog/post/list.html',{'posts': posts,'page':page})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                            status='published',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    return render(request,
                    'blog/post/detail.html',
                    {'post': post})

#class based views

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

#end for class based views