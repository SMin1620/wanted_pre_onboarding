from django.urls import path, include

from post.views import (
    PostListCreateAPI,
    PostDetailUpdateDeleteAPI,
)


post_list = PostListCreateAPI.as_view({
    'get': 'list',
    'post': 'create'
})

post_detail = PostDetailUpdateDeleteAPI.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy',
})

post_support = PostDetailUpdateDeleteAPI.as_view({
    'post': 'support'
})


urlpatterns = [
    path('', post_list),
    path('<int:post_id>/', post_detail),
    path('<int:post_id>/support/', post_support)
]


