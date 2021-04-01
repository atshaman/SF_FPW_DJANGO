# from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import Post
import datetime

class PostsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-created_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.datetime.utcnow()
        return context


class PostDetails(DetailView):
    model = Post
    template_name = 'newsone.html'
    context_object_name = 'post'
