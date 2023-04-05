from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
## create our database tables


##create python classes to represent database table


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")

    def __str__(self):
        return self.user.username


def create_profile(sender,instance,created,**kwargs):
    if(created):
        user_profile = Profile(user=instance)
        user_profile.save()
        # user_profile.name.set([instance.profile.user.username])
        # user_profile.save()
post_save.connect(create_profile, sender=User)


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    # user = 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    #one to many relationship here, one room can have many messages, but messages can only have one room
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
