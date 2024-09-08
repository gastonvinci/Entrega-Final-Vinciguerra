from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm

def blog_list(request):
    form = BlogSearchForm(request.GET)
    blogs = Blog.objects.all()
    
    if form.is_valid():
        query = form.cleaned_data['query']
        blogs = blogs.filter(title__icontains=query) | blogs.filter(body__icontains=query)
    
    return render(request, 'pages/blog_list.html', {'blogs': blogs, 'form': form})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'pages/blog_detail.html', {'blog': blog})

def blog_create(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm()
    return render(request, 'pages/blog_form.html', {'form': form})

def blog_search(request):
    form = BlogSearchForm(request.GET)
    blogs = Blog.objects.all()
    
    if form.is_valid():
        query = form.cleaned_data['query']
        blogs = blogs.filter(title__icontains=query) | blogs.filter(body__icontains=query)
    
    return render(request, 'pages/blog_list.html', {'blogs': blogs, 'form': form})