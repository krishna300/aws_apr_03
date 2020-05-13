from django.db import models
from django.db.models.signals import post_save
from PIL import Image
from django.contrib.auth.models import User



class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profilePics',default='default.jpg')


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        img=Image.open(self.image.path)
        if img.height > 300 or img.width > 300 :
            output_size =(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


def profile_update(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
    kwargs['instance'].profile.save()


post_save.connect(profile_update, sender=User)
