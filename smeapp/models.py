from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Photos(models.Model):
    image1 = CloudinaryField('image')
    image2 = CloudinaryField('image')
    image3 = CloudinaryField('image')
    image4 = CloudinaryField('image')
    image5 = CloudinaryField('image')
    image6 = CloudinaryField('image')
    image7 = CloudinaryField('image')
    image8 = CloudinaryField('image')
    image9 = CloudinaryField('image')