"""OnlionEducation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin
from django.views.static import serve

from users.views import *
from organization.views import *
from OnlionEducation.settings import MEDIA_ROOT
# from OnlionEducation.settings import STATIC_ROOT
urlpatterns = [

    #后台
    url(r'^xadmin/', xadmin.site.urls),

    #主页
    url('^$',TemplateView.as_view(template_name="index.html"),name="index"),

    #登录
    url('^login/$', LoginView.as_view(), name="login"),

    #登出
    url('^logout/$', LogoutView.as_view(), name="logout"),

    #注册页
    url('^register/$', RegisterView.as_view(), name="register"),

    # 验证码
    url(r'^captcha/', include('captcha.urls')),

    #激活账号链接
    url(r'^active/(?P<active_code>.*)/$', AciveUserView.as_view(), name="user_active"),

    #忘记密码登录页面
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),

     # active_code接收（.*） （重置密码链接）
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),

    #修改密码链接
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),

    #课程机构url配置
    url(r'^org/', include('organization.urls', namespace="org")),

    # 课程相关url配置
    url(r'^course/', include('courses.urls', namespace="course")),

    #配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$',  serve, {"document_root":MEDIA_ROOT}),

    #静态文件设置，生产环境中不起用
    # url(r'^static/(?P<path>.*)$',  serve, {"document_root":STATIC_ROOT}),

    #课程相关url配置
    url(r'^users/', include('users.urls', namespace="users")),

    #富文本相关url
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
]

#全局404，500页面配置
handler404 = 'users.views.page_not_found'  # debug=False启用
handler500 = 'users.views.page_error'