from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter

from post.models import Post
from post.serializers import (
    PostListSerializer,
    PostCreateUpdateSerializer,
    PostDetailSerializer,
    SupportSerializer
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
        elif self.request.method == 'POST':
            return SupportSerializer
        else:
            return PostCreateUpdateSerializer

    # 지원 기능
    @action(detail=True, methods='post')
    def support(self, request, *args, **kwargs):
        user = self.request.user
        pk = self.kwargs['post_id']
        post = get_object_or_404(Post, pk=pk)

        # 지원 하기
        post.supported_user.add(user)

        return Response(status=status.HTTP_201_CREATED)




