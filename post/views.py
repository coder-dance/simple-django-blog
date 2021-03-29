from django.shortcuts import render
from post.models import Post
from django.core.paginator import Paginator
import math
# Create your views here.
# 渲染主页面
import django.conf.global_settings

def query_all(request, page=1):
    page = int(page)

    post_list = Post.objects.all().order_by('-created')

    # 创建分页器对象
    page_obj = Paginator(post_list, 1)
    # 获取当前页的数据
    per_page_list = page_obj.page(page)

    # 生成页码数
    # 每页开始页码
    begin = (page - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1
    # 每页结束页码
    end = begin + 9
    if end > page_obj.num_pages:
        end = page_obj.num_pages
    if end <= 10:
        begin = 1
    else:
        begin = end - 9

    page_list = range(begin, end + 1)

    return render(request, "index.html", {'post_list': per_page_list, 'page_list': page_list, 'current_page': page})


# 阅读全文
def detail(request, id):
    post_id = int(id)

    # 根据 post_id 查询帖子的详情
    post = Post.objects.get(id=id)

    return render(request, 'detail.html', {'post': post})


# 根据类别id查询所有帖子
def query_post_by_cid(request, cid):
    post_list = Post.objects.filter(category_id=cid)
    return render(request, 'article.html', {'post_list': post_list})


# 根据发帖时间查询所有帖子
def query_post_by_created(request, year=None, month=None):
    if all([year, month]):
        post_list = Post.objects.filter(created__year=year, created__month=month)
    else:
        post_list = Post.objects.all().order_by('-created')
    return render(request, 'article.html', {'post_list': post_list})


def about(request):
    return render(request, 'about.html')