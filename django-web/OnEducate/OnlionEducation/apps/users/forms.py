# -*- coding: utf-8 -*-

__author__ = "zxl"
__date__ = "2018/2/22/022 11:30"

from django import forms
from captcha.fields import CaptchaField

from users.models import UserProfile

#对提交的表单进行预处理

class LoginForm(forms.Form):
    """
    登录表单
    """
    username = forms.CharField(required=True)  # 与html中的name字段必须相同
    password = forms.CharField(required=True,min_length=5)


class RegisterForm(forms.Form):
    """
    注册表单
    """
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})


class ForgetForm(forms.Form):
    """
    发送验证码表单（忘记密码）
    """
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})


class ModifyPwdForm(forms.Form):
    """
    修改密码表单
    """
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)

class UploadImageForm(forms.ModelForm):
    """
    上传图片头像表单
    """
    class Meta:
        model = UserProfile
        fields = ['image']


class UserInfoForm(forms.ModelForm):
    """
    用户信息表单
    """
    class Meta:
        model = UserProfile
        fields = ['nick_name', 'gender', 'birday', 'address', 'mobile']