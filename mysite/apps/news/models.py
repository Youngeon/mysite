from django.db import models
from datetime import date
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class Articles(models.Model):
    title = models.CharField(max_length = 120)
    post = models.TextField() 
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.date >= (timezone.now() - datetime.timedelta(days = 1))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    article = models.ForeignKey(Articles, on_delete = models.CASCADE)
    author_name = models.CharField('Имя автора', max_length= 50)
    comment_text = models.CharField('Текст комментария', max_length= 200)
    author = models.ForeignKey(User,on_delete= models.CASCADE)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
