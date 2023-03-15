from django.shortcuts import render
from .models import Post
from django.http import Http404
from django.shortcuts import render, get_object_or_404


def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'list.html',
                  {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post,
                             id=id,
                             status=Post.Status.PUBLISHED)
    return render(request,'detail.html',{ 'post': post})