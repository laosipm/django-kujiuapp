# -*- coding: utf-8 -*-
from  django import template
from ..models import Post, Category

# 实例化了一个 template.Library 类。
register = template.Library()

# 编写获取数据库前 N 篇文章，默认 N=5。
# 按照Django规定通过template模块来注册这个函数为模板标签。将 get_recent_posts 装饰为 register.simple_tag。
# Django1.9之后的版本才支持 simple_tag 模板标签。
# FIXME 已经将 Django 从 Django1.8 升级到 1.11.23 版本。需要研究 Django1.8 如何注册模板。
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

# 编写最新文章模板归档函数并注册为模板标签。
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

# 编写分类模板标签。
@register.simple_tag
def get_categories():
    return Category.objects.all()