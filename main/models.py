from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	image = models.ImageField(upload_to='posts')
	date_posted =models.DateTimeField(default= timezone.now)
	caption = models.TextField()
	author = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.author} --> post'

	# def get_absolute_url(self):
	# 	return reverse('index')
	# 	# return reverse('post-detail',kwargs={'pk':self.pk})

	# 	# reverse('view name') will return the full pth to the view