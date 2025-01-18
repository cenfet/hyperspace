from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404
from . models import Blog
def blog_list(request):
    blogs = Blog.objects.all()

    paginator = Paginator(blogs,1)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/blog_list.html',{'page_obj':page_obj})

def blog_detail(request,slug):
    blog = get_object_or_404( Blog,slug=slug)
    return render(request, 'blog/blog_dtl.html',{'blog':blog})