from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('explore/', views.ExploreView.as_view(), name='explore'),
    path('tweet/<int:pk>/', views.TweetDetailView.as_view(), name='tweet-detail'),
    path('tweet/new/', views.TweetCreateView.as_view(), name='tweet-create'),
    path('tweet/<int:pk>/update/', views.TweetUpdateView.as_view(), name='tweet-update'),
    path('tweet/<int:pk>/delete/', views.TweetDeleteView.as_view(), name='tweet-delete'),
    path('tweet/<int:pk>/comment/', views.add_comment, name='add-comment'),
    path('tweet/<int:pk>/like/', views.like_tweet, name='like-tweet'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete-comment'),
    path('search/', views.search, name='search'),
]
