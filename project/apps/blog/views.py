# Create your views here.

from .models import Blog, Category
from django.shortcuts import render, render_to_response, get_object_or_404



def index(request):
    items = Blog.objects.all() # add [:1] to show only the first object
    categories = Category.objects.all()
    return render(request, 'blog/index.html', {'categories': categories, 'posts': items}) 




def view_post(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog/view_post.html', {'post': post})



def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Blog.objects.filter(category=category)[:5]
    return render(request, 'blog/view_category.html', {'category': category, 'posts': posts})



# def index(request):
#     return render_to_response('blog/index.html', {
#         'categories': Category.objects.all(),
#         'posts': Blog.objects.all()[:5]
#     })

# def view_post(request, slug):   
#     return render_to_response('blog/view_post.html', {
#         'post': get_object_or_404(Blog, slug=slug)
#     })

# def view_category(request, slug):
#     category = get_object_or_404(Category, slug=slug)
#     return render_to_response('blog/view_category.html', {
#         'category': category,
#         'posts': Blog.objects.filter(category=category)[:5]
#     })


