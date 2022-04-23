from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from PIL import Image


# Create your models here.


class Profile(models.Model):
    # make one to one relationship b/w Profile and User Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone = models.CharField(max_length=11, null=True, blank=True)
    address = models.TextField(max_length=150, null=True, blank=True)

    def clean(self):
        if not (str(self.phone)).isnumeric():
            raise ValidationError('Invalid Phone Number')

    def __str__(self, *args, **kwargs):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()  # run save method the parent class
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            """ override the resized image and saved it in the file path"""
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
