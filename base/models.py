from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
  user = models.ForeignKey(User , on_delete=models.CASCADE)
  judul = models.CharField(max_length=256)
  deskripsi = models.TextField()
  complete = models.BooleanField(default=False)

  def __str__(self):
    return self.judul
  
  class Meta:
    ordering = ['complete']