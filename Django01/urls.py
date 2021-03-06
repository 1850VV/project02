"""Django01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

# app01/index
# index
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # 包含应用app01下的url.py文件
    # http://127.0.0.1:8080/app01/index
    # url(r'^app01/', include('app01.urls'))

    # http://127.0.0.1:8000/index
    # ^: 可以匹配任意的字符串
    url(r'^', include('app01.urls'))

]
