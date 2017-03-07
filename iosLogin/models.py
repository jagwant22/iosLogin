from __future__ import unicode_literals

from django.db import models

class UserProfile(models.Model):
	user= models.CharField(max_length = 100, null = False, blank = False)
	password = models.CharField(max_length = 50, null = False, blank = False)

	def __str__(self):
		return self.user 