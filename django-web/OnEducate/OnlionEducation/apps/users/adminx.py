# -*- coding: utf-8 -*-
__author__ = "zxl"
__date__ = "2018/2/21/021 12:31"

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _

from .models import EmailVerifyRecord, Banner, UserProfile


class UserProfileAdmin(UserAdmin): # 继承django 的useradmin （自定义user）
    """
    用户信息
    """
    def get_form_layout(self):  # 设置页面布局
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             'username', 'password',
                             css_class='unsort no_title'
                             ),
                    Fieldset(_('Personal info'),
                             Row('first_name', 'last_name'),
                             'email'
                             ),
                    Fieldset(_('Permissions'),
                             'groups', 'user_permissions'
                             ),
                    Fieldset(_('Important dates'),
                             'last_login', 'date_joined'
                             ),
                ),
                Side(
                    Fieldset(_('Status'),
                             'is_active', 'is_staff', 'is_superuser',
                             ),
                )
            )
        return super(UserAdmin, self).get_form_layout()

class BaseSetting(object):
    """
    后台模板设置
    """
    enable_themes = True  # 主题功能选线开启
    use_bootswatch = True

class GlobalSettings(object):
    """
    后台模板设置
    """
    site_title = "在线教育网后台管理系统"
    site_footer = "在线教育网"
    menu_style = "accordion"  # 收缩后台列表

class EmailVerifyRecordAdmin(object):
    """
    验证码
    """
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    # model_icon = 'fa fa-address-book-o'

class BannerAdmin(object):
    """
    轮播图
    """
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)