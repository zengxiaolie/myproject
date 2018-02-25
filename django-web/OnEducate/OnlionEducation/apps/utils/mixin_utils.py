# -*- coding: utf-8 -*-
__author__ = 'bobby'

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# django-xadmin的登陆权限设置
class LoginRequiredMixin(object):
    # login_required是函数装饰器，method_decorator可以将函数装饰器转化成方法装饰器
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)