from django.contrib.auth.models import User, AnonymousUser
from django.db import models


# Create your models here.

class User_profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    name = models.CharField(default='', max_length=64)
    picture = models.FileField(null=True, blank=True, upload_to='')
    follows = models.ManyToManyField('self', symmetrical=False, related_name='follower')
    accepted_challenges = models.ManyToManyField('Challenge')
    XP = models.IntegerField(default=0)


class Challenge(models.Model):
    challenge_id = models.UUIDField()
    creator = models.ForeignKey('User_profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512, default='')
    category = models.CharField(max_length=64, default='Fun')
    Info = models.FileField(null=True, blank=True, upload_to='')


# gherbi is the performed challenges done by users which is related to a Challenge
class gherbi(models.Model):
    performer = models.ForeignKey(to='User_profile', on_delete=models.CASCADE, related_name='performed_gherbi')
    vote = models.ManyToManyField(to='User_profile', related_name='voted_gherbi')
    media = models.FileField(upload_to='', blank=True)
    challenge = models.ForeignKey(to='Challenge', on_delete=models.CASCADE)


class Comment(models.Model):
    writer = models.ForeignKey(to='User_profile', on_delete=models.CASCADE, related_name='written_comment')
    comment = models.CharField(max_length=512)
    user = models.ForeignKey(to='User_profile', on_delete=models.CASCADE, null=True, related_name='issued_comment')
    challenge = models.ForeignKey(to='Challenge', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField()
