from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    video = models.FileField(upload_to='posts/videos/', blank=True, null=True)

    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def clean(self):
        if not self.image and not self.video:
            raise ValidationError("Post must contain image or video.")

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"