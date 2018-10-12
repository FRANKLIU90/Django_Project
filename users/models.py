from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_image')

    def __str__(self):
        return "{}'s Profile".format(self.user)

    def save(self, **kwargs): # add **kwargs , or get "save() got an unexpected keyword argument 'force_insert' "

        super().save()
        # img = Image.open(self.image.url)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.image.path)
