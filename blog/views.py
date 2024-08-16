from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):# 注意：published_dateでフィールドを作成している場合は、published_atとなっているところは全てpublished_dateにすること
    posts = Post.objects.all().order_by('published_at')
    return render(request, 'blog/post_list.html', {'posts': posts})