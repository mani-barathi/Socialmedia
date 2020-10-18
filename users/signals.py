from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import  receiver
from .models import Profile
# post_save is signal which is sent when a object is saved to db
# User send signal receiver receives the signal
# sender is User model
# instance is the User instance that just got created
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
	if created:
		profile = Profile.objects.create(user=instance)
		profile.save()

# save profile that we just created above when the user object is being saved
# @receiver(post_save,sender=User)
# def save_profile(sender,instance,**kwargs):
# 	instance.profile.save()



