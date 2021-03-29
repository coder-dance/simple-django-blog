# -*- coding: utf-8 -*-
"""
@Author  : LiuYuan
@Time    : 2021/3/21 22:08
@Software: PyCharm
@File    : myfilter.py
"""
from django.template import Library

register = Library()


@register.filter
def md(value):
    import markdown
    return markdown.markdown(value, extensions=['markdown.extensions.extra'])
