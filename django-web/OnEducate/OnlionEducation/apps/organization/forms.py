# -*- coding: utf-8 -*-
__author__ = "zxl"
__date__ = "2018/2/23/023 16:40"

import re
from django import forms

from operation.models import UserAsk


class UserAskForm(forms.ModelForm):  # 用model中的来转换

        # 这里添加需要的添加字段

    class Meta:
        model = UserAsk  # 取用UserAsk
        fields = ['name', 'mobile', 'course_name']  # 选择需要的字段

    def clean_mobile(self):  # 自定义表单验证，必须clean_开头
        """
        验证手机号码是否合法
        """
        mobile = self.cleaned_data['mobile']  # 取出当前mobile对象
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法", code="mobile_invalid")
