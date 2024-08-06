from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    keywords = models.ManyToManyField('notes.Keyword', related_name='notes')
    
class Keyword(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.CharField(max_length=255)
    
