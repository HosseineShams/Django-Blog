from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, Log


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        


@receiver(post_delete, sender=Profile)
def delete_profile_user(sender, instance, **kwargs):
    import inspect
    for fram_record in inspect.stack():
        if fram_record[3] == "get_response":
            request = fram_record[0].f_locals["request"]
            break
    else:
        request = None
    instance.user.delete()


@receiver(post_save, sender=Profile)
def update_profile_user(sender, instance, **kwargs):
    instance.user.save()