from django.urls import path
from .views import ProfileList,ProfileDetailView,SignUpView,FollowUserView,ListFollowing,home,ListExploreView

urlpatterns = [
    path('home',home,name='home'),
    # path('signup/',signup_view,name='signup'),
    path('signup/',SignUpView.as_view(),name='signup'),
    path('listprofile',ProfileList.as_view(),name='profilelist'),
    path('profile/<int:pk>/',ProfileDetailView.as_view(),name='profile_detail'),
    path('follow/',FollowUserView.as_view(),name='follow'),
    path('followinglist/',ListFollowing.as_view(),name='followinglist'),
    # path('unfollow/<int:pk>/',UnfollowUserView.as_view(),name='unfollow')
    path('explore/',ListExploreView.as_view(),name='explore'),
]
