from django.urls import  path
from .views import CreatePostView,ListPostView

urlpatterns = [
    path('createpost/',CreatePostView.as_view(),name='createpost'),
    path('listpost/',ListPostView.as_view(),name='listpost'),
]

