from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from .models import Tweet, Comment, Like
from .forms import TweetForm, CommentForm
from users.models import Follow

class HomeView(ListView):
    model = Tweet
    template_name = 'tweets/home.html'
    context_object_name = 'tweets'
    ordering = ['-date_posted']
    paginate_by = 10

    def get_queryset(self):
        # If user is authenticated, show tweets from followed users + own tweets
        if self.request.user.is_authenticated:
            # Get users that the current user follows
            following_users = User.objects.filter(followers__follower=self.request.user)
            # Add the current user to the list
            users_to_display = list(following_users) + [self.request.user]
            return Tweet.objects.filter(author__in=users_to_display).order_by('-date_posted')
        # If not authenticated, show all tweets
        return Tweet.objects.all().order_by('-date_posted')

class ExploreView(ListView):
    model = Tweet
    template_name = 'tweets/explore.html'
    context_object_name = 'tweets'
    ordering = ['-date_posted']
    paginate_by = 10

class TweetDetailView(DetailView):
    model = Tweet
    template_name = 'tweets/tweet_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comments.all()

        # Check if user has liked this tweet
        if self.request.user.is_authenticated:
            context['liked'] = Like.objects.filter(tweet=self.object, user=self.request.user).exists()
        else:
            context['liked'] = False

        return context

class TweetCreateView(LoginRequiredMixin, CreateView):
    model = Tweet
    form_class = TweetForm
    template_name = 'tweets/tweet_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TweetUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tweet
    form_class = TweetForm
    template_name = 'tweets/tweet_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        tweet = self.get_object()
        return self.request.user == tweet.author

class TweetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/tweet_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        tweet = self.get_object()
        return self.request.user == tweet.author

@login_required
def add_comment(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.tweet = tweet
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment has been added!')
            return redirect('tweet-detail', pk=tweet.pk)
    else:
        form = CommentForm()

    return render(request, 'tweets/add_comment.html', {'form': form, 'tweet': tweet})

@login_required
def like_tweet(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)

    # Check if the user already liked this tweet
    like, created = Like.objects.get_or_create(tweet=tweet, user=request.user)

    if not created:
        # User already liked the tweet, so unlike it
        like.delete()
        liked = False
    else:
        # User just liked the tweet
        liked = True

    # If it's an AJAX request, return JSON response
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'liked': liked,
            'likes_count': tweet.get_likes_count()
        })

    # Otherwise redirect back to the tweet detail page
    return redirect('tweet-detail', pk=tweet.pk)

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    tweet_pk = comment.tweet.pk

    # Check if the user is the author of the comment
    if request.user == comment.author:
        comment.delete()
        messages.success(request, 'Your comment has been deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return redirect('tweet-detail', pk=tweet_pk)

def search(request):
    query = request.GET.get('q', '')

    if query:
        # Search for users
        users = User.objects.filter(username__icontains=query)

        # Search for tweets
        tweets = Tweet.objects.filter(content__icontains=query).order_by('-date_posted')
    else:
        users = User.objects.none()
        tweets = Tweet.objects.none()

    context = {
        'users': users,
        'tweets': tweets,
        'query': query
    }

    return render(request, 'tweets/search_results.html', context)
