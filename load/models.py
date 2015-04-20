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

class Caf(models.Model):
	name = models.CharField(max_length=6, unique=True, blank=False)

class Subject(models.Model):
	name = models.CharField(max_length=60, unique=True, blank=False)

class Group(models.Model):
	caf = models.ForeignKey(Caf)
	sem = models.IntegerField()
	number = models.IntegerField()
	GRADES = (
		('b','bachelor'),
		('m','master'),
		('s','specialist'),
	)
	grade = models.CharField(max_length=1,
									  choices=GRADES,
									  default='b')
	amount = models.IntegerField()

	class Meta:
		unique_together = ('caf', 'sem', 'number')

class FormPass(models.Model):
	name = models.CharField(max_length=20, unique=True, blank=False)

class TypeLoad(models.Model):
	name = models.CharField(max_length=20, unique=True, blank=False)

class LoadUnit(models.Model):
	subject = models.ForeignKey(Subject)
	caf = models.ForeignKey(Caf)
	formPass = models.ForeignKey(FormPass)
	sem = models.IntegerField()
	typeLoad = models.ForeignKey(TypeLoad)
	hours = models.IntegerField()

class Spread(models.Model):
	loadUnit = models.ForeignKey(LoadUnit)
	prof = models.ForeignKey(Professors, null=True)
	group = models.ForeignKey(Group)