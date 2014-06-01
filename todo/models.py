from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=10)
	def __unicode__(self):
		return self.username

class Note(models.Model):
	note = models.CharField(max_length=200)
	username = models.ForeignKey(User)
	timestamp = models.DateTimeField()
	category = models.CharField(max_length=10)
	def __unicode__(self):
		return '%s %s' % (self.note, self.timestamp)

class Document(models.Model):
	docfile = models.FileField(upload_to='media/images');
