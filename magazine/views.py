from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['name', 'description', 'price', 'photo']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class FullPostViews(DetailView):
    model = Post
    template_name = 'full_post.html'
