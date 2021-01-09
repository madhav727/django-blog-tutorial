from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView, View

# Create your views here.
class HomeView(View):
    def get(self, *args, **kwargs):
        posts = Post.objects.all()
        context = {
            'posts': posts,
        }
        return render(self.request, "home.html", context)

class PostDetailView(DetailView):
    model = Post
    template_name = 'post-detail.html'