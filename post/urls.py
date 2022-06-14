from django.urls import path, include

from post.views import (
    PostListCreateAPI,
    PostDetailUpdateDeleteAPI,
)

# 채용 공고 목록 페이지 <list, create>
post_list = PostListCreateAPI.as_view({
    'get': 'list',
    'post': 'create'
})

# 채용 공고 상세 페이지 <retrieve, patch, delete>
post_detail = PostDetailUpdateDeleteAPI.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy',
})

# 채용 공고 지원 <support>
post_support = PostDetailUpdateDeleteAPI.as_view({
    'post': 'support'
})


urlpatterns = [
    path('', post_list),
    path('<int:post_id>/', post_detail),
    path('<int:post_id>/support/', post_support)
]


