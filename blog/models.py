from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # on_delete=models.CASCADE: ユーザが削除されたときに投稿も削除
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        # 管理画面の設定
        return self.title
