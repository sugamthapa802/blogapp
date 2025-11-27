from django.shortcuts import render,get_object_or_404,HttpResponse,redirect,HttpResponseRedirect
from .models import CustomUser,Profile,Follow
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import Http404
from .forms import CustomUserCreationForm,CrispyAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .services.follow_service import FollowService
from django.urls import reverse_lazy
from django.contrib.auth import login,authenticate,logout

def home(request):
    return render(request,'accounts/home.html')


def login_view(request):
    if request.method=='POST':
        form=CrispyAuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
    else:
      form=CrispyAuthenticationForm()
    return render(request,'registration/login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('home')


class ProfileList(ListView):
    model = Profile
    context_object_name = 'profiles'
    template_name='accounts/profilelist.html'

class ProfileDetailView(DetailView):
    model=Profile
    context_object_name='profile'
    template_name='accounts/profiledetail.html'
    
"""
Function based views for signup :
def signup_view(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form=CustomUserCreationForm()
    return render(request,'registration/sign_up.html',{'form':form})

"""
class SignUpView(CreateView):
    form_class=CustomUserCreationForm
    template_name='registration/sign_up.html'
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save()  # MUST assign to self.object
        login(self.request, self.object)
        return redirect(self.get_success_url()) # now get_success_url() works


#Follow functionality related_works after this :

class FollowUserView(LoginRequiredMixin,View):
    success_url = reverse_lazy('home')
    def post(self,request,*args, **kwargs):
        username_to_follow=request.POST.get('username','')
        service=FollowService(current_user=request.user)
        message=service.follow_service(username_to_follow)
        return redirect(self.success_url)

def followuser(request,pk):
    user_to_follow=get_object_or_404(Profile,id=pk)
    following_user_profile_id=request.user.profile
    if user_to_follow==following_user_profile_id:
        return HttpResponse('you cannot follow yourself')
    if Follow.objects.filter(follower=following_user_profile_id,following=user_to_follow).exists():
        return HttpResponse('already exists')
    Follow.objects.create(follower=following_user_profile_id,following=user_to_follow)
    return render(request,'accounts/follow.html')
    

"""
Class UnfollowUserView(loginrequiredmixin,UpdateView):
    model=Follow
    form_class=FollowForm
    template_name='accounts/follow.html'
    success_url='home'

"""
# class UnfollowUserView(LoginRequiredMixin,View):
#     def post(self,request,*args, **kwargs):
#         username_to_unfollow=

# listing friends that you follow
class ListFollowing(LoginRequiredMixin,ListView):
    model=Follow
    template_name='accounts/following_list.html'
    context_object_name='following_list'
    
    def get_queryset(self):
        user_profile=Profile.objects.get(user=self.request.user)
        return Follow.objects.filter(follower=user_profile)

class ListExploreView(LoginRequiredMixin,ListView):
    model=Follow
    template_name='accounts/explore.html'
    context_object_name='registered_users'
    paginate_by=9
    def get_queryset(self):
        user_profile=get_object_or_404(Profile,user=self.request.user)
        queryset = Profile.objects.exclude(id=user_profile.id)
        #  Exclude users already followed
        following_profiles = Follow.objects.filter(follower=user_profile).values_list('following_id', flat=True)
        queryset = queryset.exclude(id__in=following_profiles)
        return queryset
        