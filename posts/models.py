from django.db import models
from django.contrib.auth.models import User

# CREDIT: Adapted from the Code Institute DRF Tutorial Project
# URL:    https://github.com/Code-Institute-Solutions/drf-api


class Post(models.Model):
    image_filter_choices = [
        ('art', 'Art'), ('cats', 'Cats'),
        ('dogs', 'Dogs'), ('food', 'Food'),
        ('nature', 'Nature'), ('photo', 'Photo'),
        ('travel', 'Travel'), ('wallpaper', 'Wallpaper')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_h8c5hq', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
