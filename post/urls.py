"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from post import views

urlpatterns = [
    path('', views.query_all),
    path('page/<int:page>', views.query_all),
    path('post/<int:id>', views.detail),
    path('category/<int:cid>', views.query_post_by_cid),
    path('archive/', views.query_post_by_created),
    path('archive/<int:year>/<int:month>', views.query_post_by_created),
    path('about/', views.about),
]
