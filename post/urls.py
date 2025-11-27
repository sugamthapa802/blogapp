from django.urls import  path
from .views import CreatePostView,ListOwnPostView,PostDetailView

urlpatterns = [
    path('createpost/',CreatePostView.as_view(),name='createpost'),
    path('list_own_post/',ListOwnPostView.as_view(),name='list_own_post'),
    path('post_detail/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
]

