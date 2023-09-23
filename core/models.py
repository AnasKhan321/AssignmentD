from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class uimage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.user.username