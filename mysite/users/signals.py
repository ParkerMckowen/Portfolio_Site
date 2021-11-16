from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	# if a user is created, then create a profile with the user being the instance passed
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
	# if a user is saved, then save the profile according to the current instance of user
	instance.profile.save()