from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Tweet(models.Model):
    content = models.TextField(max_length=280)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    image = models.ImageField(upload_to='tweet_images', blank=True, null=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.content[:50]

    def get_absolute_url(self):
        return reverse('tweet-detail', kwargs={'pk': self.pk})

    def get_likes_count(self):
        return self.likes.count()

    def get_comments_count(self):
        return self.comments.count()

class Comment(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=280)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f'Comment by {self.author.username} on {self.tweet}'

class Like(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('tweet', 'user')

    def __str__(self):
        return f'{self.user.username} likes {self.tweet}'
