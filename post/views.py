from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from post.models import Post
from post.serializers import (
    PostListSerializer,
    PostCreateUpdateSerializer,
)


# Create your views here.
# 공고 목록, 생성 뷰
class PostListCreateAPI(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    def get_queryset(self):
        return Post.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostListSerializer
        else:
            return PostCreateUpdateSerializer


# # 공고 상세, 수정 뷰
# class PostDetailUpdateAPI(mixins.RetrieveModelMixin,
#                           mixins.UpdateModelMixin,
#                           viewsets.GenericViewSet):
#     lookup_url_kwarg = 'post_id'
#
#     def get_queryset(self):
#         return Post.objects.all()


