from django.db import models
from userApp.models import Profil

class Maqola(models.Model):
    sarlavha=models.CharField(max_length=255)
    batafsil=models.TextField()
    rasm=models.ImageField(upload_to="maqolalar/",blank=True,null=True)
    sana=models.DateTimeField(auto_now_add=True)
    korish=models.PositiveIntegerField(default=0)
    profil=models.ForeignKey(Profil,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return f"{self.profil.username}:{self.sarlavha}"

