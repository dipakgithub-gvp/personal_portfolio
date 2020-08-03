from django.shortcuts import render
from . models import Blog

# Create your views here.
def blog_index(request):
    blogs = Blog.objects.order_by('-date')
    return render(request,'blog/blog_index.html',{"blogs":blogs})