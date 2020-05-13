from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    url = models.URLField(null=True)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('list')