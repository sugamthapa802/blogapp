from accounts. models import Follow,Profile,CustomUser
from django.shortcuts import get_object_or_404,HttpResponse

class FollowService:
    def __init__(self,current_user):
        self.current_user=current_user
    
    def follow_service(self,username_to_follow):
        username_to_follow=username_to_follow.strip()
        if not username_to_follow:
            return HttpResponse('Please provide username')
        user_to_follow = get_object_or_404(CustomUser, username=username_to_follow)
        if self.current_user==user_to_follow:
            return HttpResponse('You cannot follow yourself.')
        follower_profile=self.current_user.profile
        profile_to_follow=Profile.objects.get(user=user_to_follow)
        if Follow.objects.filter(follower=follower_profile,following=profile_to_follow).exists():
            return HttpResponse('You already follow this user!')
        Follow.objects.create(follower=follower_profile,following=profile_to_follow)
        return HttpResponse(f'Successfully followed the user{profile_to_follow}!')
    
    def unfollow_service(self,username_to_unfollow):
        pass