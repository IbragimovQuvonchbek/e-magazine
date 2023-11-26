from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    

class CreatePostView(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['name', 'description', 'price', 'photo']
