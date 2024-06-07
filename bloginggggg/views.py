# bloginggggg/views.py

from django.shortcuts import render, get_object_or_404
from .models import Blogpost

def show_blogpost_list(request):
    posts = Blogpost.objects.all()
    context = {'posts': posts}
    return render(request, 'bloginggggg/blogpost_list.html', context)

def show_blogpost_detail(request, pk):
    post = get_object_or_404(Blogpost, pk=pk)
    context = {'post': post}
    return render(request, 'bloginggggg/blogpost_detail.html', context)
