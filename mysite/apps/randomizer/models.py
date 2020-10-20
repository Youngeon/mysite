from django.db import models

class Randomizer(models.Model):
    word = models.CharField(max_length=30)
    def __srt__(self):
        return self.word
class Item1(models.Model):
    word = models.CharField(max_length=30)
