from django.db import models

class Posts(models.Model):
	name = models.CharField(max_length=20, unique=True, blank=False)

class Degrees(models.Model):
	name = models.CharField(max_length=20, unique=True, blank=False)

class Professors(models.Model):
	first_name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=20)
	middle_name = models.CharField(max_length=20)
	post = models.ForeignKey(Posts)
	degree = models.ForeignKey(Degrees)
	note = models.CharField(max_length=127)
