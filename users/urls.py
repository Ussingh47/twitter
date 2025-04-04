from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html', next_page='home'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/<str:username>/', views.user_profile, name='user-profile'),
    path('profile/<str:username>/follow/', views.follow_user, name='follow-user'),
    path('profile/<str:username>/unfollow/', views.unfollow_user, name='unfollow-user'),
    path('profile/<str:username>/followers/', views.followers_list, name='followers-list'),
    path('profile/<str:username>/following/', views.following_list, name='following-list'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]
