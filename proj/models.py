from django.db import models

# Create your models here.
class Proj(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	technology = models.CharField(max_length=20)
	image = models.FilePathField(path='/img')
	website = models.CharField(default='default_value', max_length=255)



	