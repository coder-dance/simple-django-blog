from django.contrib import admin
from .models import *
# Register your models here.


class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')


admin.site.site_header = '个人博客后台管理'
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostModelAdmin)
