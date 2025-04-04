from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Follow
from tweets.models import Tweet

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    tweets = Tweet.objects.filter(author=request.user).order_by('-date_posted')

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'tweets': tweets
    }
    return render(request, 'users/profile.html', context)

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    tweets = Tweet.objects.filter(author=user).order_by('-date_posted')

    # Check if the current user follows this user
    is_following = False
    if request.user.is_authenticated:
        is_following = Follow.objects.filter(follower=request.user, following=user).exists()

    followers_count = user.followers.count()
    following_count = user.following.count()

    context = {
        'user_profile': user,
        'tweets': tweets,
        'is_following': is_following,
        'followers_count': followers_count,
        'following_count': following_count
    }
    return render(request, 'users/user_profile.html', context)

@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)

    # Don't allow users to follow themselves
    if request.user == user_to_follow:
        messages.warning(request, "You can't follow yourself.")
        return redirect('user-profile', username=username)

    # Check if already following
    follow_relation, created = Follow.objects.get_or_create(
        follower=request.user,
        following=user_to_follow
    )

    if created:
        messages.success(request, f'You are now following {username}!')
    else:
        messages.info(request, f'You are already following {username}.')

    return redirect('user-profile', username=username)

@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(User, username=username)

    # Try to find the follow relationship
    try:
        follow = Follow.objects.get(follower=request.user, following=user_to_unfollow)
        follow.delete()
        messages.success(request, f'You have unfollowed {username}.')
    except Follow.DoesNotExist:
        messages.info(request, f'You were not following {username}.')

    return redirect('user-profile', username=username)

@login_required
def followers_list(request, username):
    user = get_object_or_404(User, username=username)
    followers = user.followers.all()

    context = {
        'user_profile': user,
        'followers': followers,
        'title': f'People following {username}'
    }
    return render(request, 'users/follow_list.html', context)

@login_required
def following_list(request, username):
    user = get_object_or_404(User, username=username)
    following = user.following.all()

    context = {
        'user_profile': user,
        'following': following,
        'title': f'People {username} follows'
    }
    return render(request, 'users/follow_list.html', context)
