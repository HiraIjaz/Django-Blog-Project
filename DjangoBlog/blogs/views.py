from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.utils import timezone
from django import forms


class BlogHomeView(ListView):
    """View for displaying the list of blog posts on the home page."""
    model = Post
    template_name = 'blog/blog-home.html'

    def get_context_data(self, **kwargs):
        """
        Retrieve and return the context data for rendering the template.

        Returns:
            dict: A dictionary containing context data.
        """
        context = super().get_context_data(**kwargs)
        context['name'] = self.request.user
        return context


@method_decorator(login_required, name='dispatch')
class UserPostsView(ListView):
    """View for displaying a list of posts authored by the current user."""
    model = Post
    template_name = 'blog/user-posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        """
        Get and return the queryset containing posts authored by the current user.

        Returns:
            QuerySet: A queryset containing filtered posts.
        """
        user = self.request.user
        queryset = Post.objects.filter(author=user).order_by('date_posted').reverse()
        return queryset

    def get_context_data(self, **kwargs):
        """
        Retrieve and return the context data for rendering the template.

        Returns:
            dict: A dictionary containing context data.
        """
        context = super().get_context_data(**kwargs)
        context['name'] = self.request.user
        return context


class CommentForm(forms.ModelForm):
    """Form for adding comments to blog posts."""

    class Meta:
        model = Comment
        fields = ['text']


class PostDetailsView(DetailView):
    """View for displaying details of a single blog post."""
    model = Post
    template_name = 'blog/post-details.html'

    def get_context_data(self, **kwargs):
        """
        Retrieve and return the context data for rendering the template.

        Returns:
            dict: A dictionary containing context data.
        """
        context = super().get_context_data(**kwargs)
        context['name'] = self.request.user
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        """
        Handle the submission of a comment form.

        Args:
            request: The HTTP request object.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HttpResponse: A redirect response.
        """
        post = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.writer = self.request.user
            comment.save()
            return redirect('post-details', pk=post.pk)
        context = self.get_context_data(object=post, comment_form=form)
        return self.render_to_response(context)


@method_decorator(login_required, name='dispatch')
class CreatePostView(CreateView):
    """View for creating a new blog post."""
    model = Post
    template_name = 'blog/create-post.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('user-posts')

    def get_context_data(self, **kwargs):
        """
        Retrieve and return the context data for rendering the template.

        Returns:
            dict: A dictionary containing context data.
        """
        context = super().get_context_data(**kwargs)
        context['name'] = self.request.user
        return context

    def form_valid(self, form):
        """
        Handle the validation and saving of the form.

        Args:
            form: The form instance.

        Returns:
            HttpResponse: A redirect response.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    """View for editing an existing blog post."""
    model = Post
    template_name = 'blog/edit-post.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('user-posts')

    def get_context_data(self, **kwargs):
        """
        Retrieve and return the context data for rendering the template.

        Returns:
            dict: A dictionary containing context data.
        """
        context = super().get_context_data(**kwargs)
        context['name'] = self.request.user
        return context

    def form_valid(self, form):
        """
        Handle the validation and saving of the form.

        Args:
            form: The form instance.

        Returns:
            HttpResponse: A redirect response.
        """
        form.instance.last_edited = timezone.now()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    """View for deleting an existing blog post."""
    model = Post
    template_name = 'blog/delete-post.html'
    success_url = reverse_lazy('user-posts')
    fields = ['title', 'content']

    def get_context_data(self, **kwargs):
        """
        Retrieve and return the context data for rendering the template.

        Returns:
            dict: A dictionary containing context data.
        """
        context = super().get_context_data(**kwargs)
        context['name'] = self.request.user
        return context
