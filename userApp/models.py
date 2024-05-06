from django.db import models
from django.contrib.auth.models import AbstractUser


class Profil(AbstractUser):
    t_sana=models.DateField(blank=True,null=True)
    davlat=models.CharField(max_length=30,blank=True,null=True)

    def __str__(self):
        return self.username


