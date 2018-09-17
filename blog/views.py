from django.shortcuts import render

from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# from django.views.generic import ListView
# class PostListView(ListView):
#     model = Post
#     context_object_name = 'posts'
#     template_name = 'blog/home.html'
