from django.shortcuts import render, get_object_or_404
from . models import Blog

# Create your views here.
def blog_index(request):
    blogs = Blog.objects.order_by('-date')
    return render(request,'blog/blog_index.html',{"blogs":blogs})

def blog_post(request,blog_id):
    # posts = Blog.objects.filter(sr_no=sr_no)
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "blog/blog_post.html",{"blog":blog})   