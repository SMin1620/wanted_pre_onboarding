from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.filters import SearchFilter

from post.models import Post
from post.serializers import (
    PostListSerializer,
    PostCreateUpdateSerializer,
    PostDetailSerializer,
)


# Create your views here.
# 공고 목록, 생성 뷰
class PostListCreateAPI(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['position', 'company__company_name', 'skill']

    def get_queryset(self):
        return Post.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostListSerializer
        else:
            return PostCreateUpdateSerializer


# 공고 상세, 수정 뷰
class PostDetailUpdateDeleteAPI(mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    lookup_url_kwarg = 'post_id'

    def get_queryset(self):
        return Post.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostDetailSerializer
        else:
            return PostCreateUpdateSerializer


# # 검색
# class PostSearchAPI(viewsets.GenericViewSet):
#     def get_queryset(self):
#         if self.request.method == 'GET':


