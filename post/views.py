from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter

from company.models import Company
from post.models import Post, Support
from post.serializers import (
    PostListSerializer,
    PostCreateUpdateSerializer,
    PostDetailSerializer,
    SupportSerializer,
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

    # create
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)




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

    # action == 'retrieve 일때,
    def retrieve(self, request, *args, **kwargs):
        pk = kwargs['post_id']
        post = get_object_or_404(Post, pk=pk)

        # 채용 공고 상세 페이지에서 회사 pk 구한다.
        company = Company.objects.get(pk=post.company_id)
        # 회사 pk에 맞는 채용 공고들을 필터링해서 pk값을 리스트로 한다.
        post_in_company = Post.objects.filter(company_id=company.id).values_list('id', flat=True)

        response = Response(status=status.HTTP_200_OK)

        # 기존 시리얼라이저 데이터터
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response.data = serializer.data

        res = {
            'result': response.data,
            'posts': post_in_company
        }

        return Response(res)

    # 지원 기능
    @action(detail=True, methods='post')
    def support(self, request, *args, **kwargs):
        user = self.request.user.id
        pk = self.kwargs['post_id']
        post = get_object_or_404(Post, pk=pk)

        # 지원 하기
        # 지원 유저가 같은 공고에 지원하지 않았다면,
        if not Support.objects.filter(
            user_id=user,
            post=post
        ).exists():
            sup = Support.objects.create(
                user_id=user,
                post=post
            )
            sup.save()

            response = Response(status=status.HTTP_200_OK)
            serializer = SupportSerializer(sup, read_only=True)
            response.data = serializer.data
            print(response)
            return response
        # 지원 유저가 해당 공고에 이미 지원하였다면,
        else:
            return Response({'message': '이미 지원을 하였습니다.'})




