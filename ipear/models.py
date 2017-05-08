from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

'''
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	first_Name = models.CharField(max_length=40)
	last_Name = models.CharField(max_length=40)

	age = models.PositiveIntegerField(null=True)
	height = models.PositiveIntegerField(null=True)
	weight = models.PositiveIntegerField(null=True)	
	gender = models.CharField(max_length=40)

	address = models.CharField(max_length=100)
	phone_Number = models.CharField(max_length=11)
	
	pets = models.TextField()
	allergies = models.TextField()
	existing_Conditions = models.TextField()
	firearms = models.TextField()
	
	isDispatcher = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

def __str__(self):
	return self.user


class DispatcherInfo(models.Model):
	username = models.CharField(max_length=40, unique=True)
	password = models.CharField(max_length=50)

	first_Name = models.CharField(max_length=40)
	last_Name = models.CharField(max_length=40)

	isDispatcher = models.BooleanField(default=True)

def __str__(self):
	return self.username

'''
