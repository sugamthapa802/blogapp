from django.shortcuts import render
from .models import Post,Interactions,Like,Comment
from django.views.generic import CreateView
from .forms import PostForm
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class CreatePostView(CreateView):
    form_class=PostForm
    template_name='post/create_post.html'
    # success_url=reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class ListOwnPostView(LoginRequiredMixin,ListView):
    model=Post
    template_name='post/list_own_post.html' 
    context_object_name='posts'
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

class PostDetailView(DetailView):
    model=Post
    template_name='post/post_detail.html'
    context_object_name='post'

