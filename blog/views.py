from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm
from django.contrib import messages


def search(request):
    context = {}
    search_input = request.GET.get("search_text")
    posts = Post.objects.filter(title__contains=search_input)
    context['posts'] = posts
    context["is_ajax"] = True
    return render(request, "blog/search_results.html", context)


def home(request):
    context = {}
    template_name = 'blog/home.html'


    if request.method == 'GET':
        search_input = request.GET.get("search", "None")
        if search_input:
            posts = Post.objects.filter(title__contains=search_input)
            context['posts'] = posts
            return render(request, template_name, context)


    return render(request, template_name, context)


@login_required()
def blog(request):
    context = {}
    context["posts"] = Post.objects.all()
    template_name = 'blog/blog.html'

    return render(request, template_name, context)


def blog_details(request, slug):
    context = {}
    post = get_object_or_404(Post, slug=slug)
    context['post'] = post
    context['comments'] = post.comments.filter(status=1)
    template_name = 'blog/blog_details.html'
    return render(request, template_name, context)


@login_required()
def add_blog(request):
    context = {}
    template_name = 'blog/add-blog.html'
    initial = {
        'title': "new title",
    }

    form = BlogPostForm(request.POST or None, request.FILES or None, initial=initial)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = request.user.profile
            form.save()
            messages.success(request, 'Your post has been created!')
            return redirect('blog:add-blog')
        else:
            context['form'] = form
            return render(request, template_name, context)
    else:   
        context['form'] = form
        

    return render(request, template_name, context)