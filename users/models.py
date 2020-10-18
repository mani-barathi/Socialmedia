from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	# have one to one realtionship with user 
	# on cascade if user is deleted , delete Profile	
	image = models.ImageField(default='default.jpg',upload_to='profile_pics')
	bio = models.TextField()

	def __str__(self):
		return f'{self.user.username} --> Profile'

	# to resive the profile image 
	def save(self,*args, **kwargs):
		super().save()
		image = Image.open(self.image.path)
		if image.height > 300 or image.width>300:
			output_size = (300,300)
			image.thumbnail(output_size)
			image.save(self.image.path)