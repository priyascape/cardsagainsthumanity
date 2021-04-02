from django.db import models
from datetime import datetime
import re

# Create your models here.

class PlayerManager(models.Manager):
    def basic_validations(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "Name should be atleast 2 characters"
        return errors 

class Player(models.Model):
    name = models.CharField(max_length=45)
    is_human = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=PlayerManager()
    
class BlackCard(models.Model):
    question= models.CharField(max_length=45)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
class WhiteCard(models.Model):
    answer= models.CharField(max_length=45)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
class Score(models.Model):
    tally = models.IntegerField(default=0)
    player = models.ForeignKey(Player, related_name='scores', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
