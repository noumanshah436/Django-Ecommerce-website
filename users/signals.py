from django.db.models.signals import post_save  # we will use signal to make profile if new user is created
from django.contrib.auth.models import User  # sender ( sending the signal )
from django.dispatch import receiver
from .models import Profile


# this create_profile function is the receiver and it will get called every time a user is created
# and this function will create the profile for that user
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# this create_profile function is the receiver and it will get called every time a user is saved
# and this function will save the profile ( if that user is saved )
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # instance is our user
    instance.profile.save()

#  we also need to import signals in our user app.py file ready function
