from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from django_jalali.db import models as jmodels


MALE="m"
FEMALE="f"
OTHER="o"
PROFILE_GENDER_CHOICES = [
    (MALE,"آقا"),
    (FEMALE,"خانم"),
    (OTHER,"سایر")
]


class Log(models.Model):
    created_at = jmodels.jDateTimeField(auto_now_add=True, editable=False)
    description = models.TextField()



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="کاربر") 
    bio = models.TextField(verbose_name="بیوگرافی", null=True, blank=True, validators=[MinLengthValidator(10)])
    phone = models.CharField(verbose_name="شماره تلفن", max_length=11, help_text="همراه با صفر وارد شود", null=True, blank=True)
    gender = models.CharField(verbose_name="جنسیت", max_length=1, choices=PROFILE_GENDER_CHOICES)
    avatar = models.ImageField(verbose_name="آواتار", upload_to="acounts/avatars/", null=True, blank=True)
    nc = models.CharField(verbose_name="کد ملی", max_length=11)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "پروفایل"
        verbose_name_plural = "پروفایل ها"




