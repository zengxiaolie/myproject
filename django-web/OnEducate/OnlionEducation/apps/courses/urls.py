# -*- coding: utf-8 -*-
__author__ = "zxl"
__date__ = "2018/2/23/023 17:02"

from django.conf.urls import url, include

from .views import *

urlpatterns = [
    #课程列表页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),

    #课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),

    #课程章节信息
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_info"),

    #课程评论
    url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name="course_comments"),

    #添加课程评论
    url(r'^add_comment/$', AddComentsView.as_view(), name="add_comment"),

    #视频
    url(r'^video/(?P<video_id>\d+)/$',VideoPlayView.as_view(),name="video_play")

]