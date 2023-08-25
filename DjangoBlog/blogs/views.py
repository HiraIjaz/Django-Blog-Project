from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.utils import timezone


# Create your views here.
class BlogHomeView(ListView):
    model = Post
    template_name = 'blog/blog-home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.request.user
        return context


class UserPostsView(ListView):
    model = Post
    template_name = 'blog/user-posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        queryset = Post.objects.filter(author=user).order_by('date_posted').reverse()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.request.user
        return context


class PostDetailsView(DetailView):
    model = Post
    template_name = 'blog/post-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.request.user
        return context


class CreatePostView(CreateView):
    model = Post
    template_name = 'blog/create-post.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('user-posts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.request.user
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPostView(UpdateView):
    model = Post
    template_name = 'blog/edit-post.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('user-posts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.request.user
        return context

    def form_valid(self, form):
        form.instance.last_edited = timezone.now()
        return super().form_valid(form)


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete-post.html'
    success_url = reverse_lazy('user-posts')
    fields = ['title', 'content']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.request.user
        return context


