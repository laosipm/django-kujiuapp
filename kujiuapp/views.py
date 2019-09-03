

# Create your views here.

import markdown
from django.shortcuts import render, get_object_or_404
from comments.forms import CommentForm
from .models import Post, Category

# 定义首页文章列表视图函数。
def index(request):
    post_list = Post.objects.all()
    return render(request,'kujiuapp/index.html',context={'post_list': post_list})

# 定义文章详情页面内容视图函数。
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()
    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染响应数据。
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }

    return render(request, 'kujiuapp/detail.html', context=context)

# 定义归档页面文章列表函数。使用模型管理器（objects）的 filter 函数用来过滤文章。
def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'kujiuapp/index.html', context={'post_list': post_list})

# 定义分类页面文章列表函数。
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'kujiuapp/index.html', context={'post_list':post_list})