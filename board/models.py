from django.db import models
from django.utils import timezone
from account.models import User

# Create your models here.
class Board(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    blog = models.ForeignKey(Board, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, null=False, blank=False)
    comment = models.TextField()

    def __str__(self):
        return self.comment
