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
	name = models.CharField(max_length=127, unique=True, blank=False)

class Group(models.Model):
	caf = models.ForeignKey(Caf)
	sem = models.IntegerField()
	number = models.IntegerField()
	GRADES = (('b','b'),('m','m'),('s','s'))
	grade = models.CharField(max_length=1, choices=GRADES,default='b')
	amount = models.IntegerField()

	class Meta:
		unique_together = ('caf', 'sem', 'number')

class FormPass(models.Model):
	name = models.CharField(max_length=20, unique=True, blank=False)

class TypeLoad(models.Model):
	name = models.CharField(max_length=20, unique=True, blank=False)
	GRADES = (('all','all'),('sub','subgroup'),('non','usual'))
	typeTL = models.CharField(max_length=3, choices=GRADES,default='non')

class LoadUnit(models.Model):
	subject = models.ForeignKey(Subject)
	caf = models.ForeignKey(Caf)
	formPass = models.ForeignKey(FormPass)
	sem = models.IntegerField()
	typeLoad = models.ForeignKey(TypeLoad)
	GRADES = (('b','b'),('m','m'),('s','s'))
	grade = models.CharField(max_length=1, choices=GRADES,default='b')
	hours = models.IntegerField()

class Spread(models.Model):
	loadUnit = models.ForeignKey(LoadUnit)
	group = models.ForeignKey(Group, null=True)
	prof = models.ForeignKey(Professors, null=True)