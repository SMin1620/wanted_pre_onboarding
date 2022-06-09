from django.urls import path, include

from post.views import PostListCreateAPI


post_list = PostListCreateAPI.as_view({
    'get': 'list',
    'post': 'create'
})


urlpatterns = [
    path('', post_list),
]


