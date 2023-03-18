from django.shortcuts import render
from .models import Post
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'list.html'

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day
                             )
    return render(request,'detail.html',{ 'post': post})