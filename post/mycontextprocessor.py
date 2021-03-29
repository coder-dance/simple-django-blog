# -*- coding: utf-8 -*-
"""
@Author  : LiuYuan
@Time    : 2021/3/22 0:45
@Software: PyCharm
@File    : mycontextprocessor.py
"""
from post.models import Post
from django.db.models import Count


def get_right_info(request):
    # 1.获取分类信息
    right_category_post = Post.objects.values('category__cname', 'category').annotate(c=Count('*')).order_by('-c')

    # 2. 近期文章
    right_recent_post = Post.objects.all().order_by('-created')[:3]

    # 3.根据日期获取归档信息
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("SELECT created,count('*') c FROM t_post GROUP BY DATE_FORMAT(created,'%Y-%m') ORDER BY c DESC,created  DESC;")
    right_file_post = cursor.fetchall()

    return {'right_category_post': right_category_post, 'right_recent_post': right_recent_post,
            'right_file_post': right_file_post}
