from blog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

class PostListView(ListView):

    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):

    model = Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):

    model = Post
    template_name = 'post_new.html'
    fields = ('title', 'text')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'text']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostWarningView(TemplateView):
    model = Post
    template_name = 'warning.html'
