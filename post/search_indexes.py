# -*- coding: utf-8 -*-
"""
@Author  : LiuYuan
@Time    : 2021/3/22 16:16
@Software: PyCharm
@File    : search_indexes.py
"""
from haystack import indexes
from post.models import *


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # 给title、content设置索引
    title = indexes.NgramField(model_attr='title')
    content = indexes.NgramField(model_attr='content')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-created')
