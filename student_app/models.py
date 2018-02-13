from django.db import models
from django.utils import timezone

# Create your models here.

class School(models.Model):

	rating=(
		('one','1'),
		('two','2'),
		('three','3'),
		('four','4'),
		('five','5'),


		)
	
	name=models.CharField(max_length=50)
	address=models.CharField(max_length=200)
	rating=models.CharField(choices=rating,max_length=10)
	email=models.EmailField()
	contact_no=models.IntegerField()
	website=models.TextField(blank=True,null=True)
	enabled=models.BooleanField(default=True)
	created_date=models.DateTimeField(default=timezone.now)
	modified_date=models.DateTimeField(blank=True,null=True)


	def _str_(self):
		return self.name



class Student(models.Model):
	"""docstring for ClassName"""
	standard=(
		('five','5'),
		('six','6'),
		('seven','7'),
		('eight','8'),
		('nine','9'),
		('ten','10')



		)
	School=models.ForeignKey(School)
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email=models.EmailField()
	residence_address=models.TextField(blank=True,null=True)
	standard=models.CharField(choices=standard,max_length=50)
	roll_no=models.IntegerField()
	fees=models.DecimalField(decimal_places=3,max_digits=10)
	created_date=models.DateTimeField(default=timezone.now)
	modified_date=models.DateTimeField(blank=True,null=True)

	

	def __str__(self):
		return self.first_name
		