from django.db import models
from django.contrib.auth import get_user_model

class Thing(models.Model):
    name = models.CharField(max_length=200)
    cost = models.IntegerField()
    user = get_user_model()
    note = models.CharField(max_length=256)
    bought_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.name