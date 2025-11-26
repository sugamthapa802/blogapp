from django.urls import  path
from django.conf import settings
from django.conf.urls.static import static
from .views import CreatePostView,ListPostView

urlpatterns = [
    path('createpost/',CreatePostView.as_view(),name='createpost'),
    path('listpost/',ListPostView.as_view(),name='listpost'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)