# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
#creating house table in the database
class House(models.Model):
	house_id=models.IntegerField(primary_key=True)
	lat=models.FloatField()
	lon=models.FloatField()
	area=models.FloatField()
	isfarm=models.BooleanField()
	AnnualIncome=models.FloatField()
	def __str__(self):
		k=self.house_id
		return str(k)

#creating member details table in the database

class mem_details(models.Model):
	house_idm=models.ForeignKey(House,on_delete=models.CASCADE)
	Name=models.CharField(max_length=30)
	dob=models.DateField()
	gender=models.CharField(max_length=35)
	uid=models.IntegerField(unique=True)
	def __str__(self):
		return self.Name

#creating images table in the database

class imagetable(models.Model):
	house_idi=models.ForeignKey(House,on_delete=models.CASCADE)
	image=models.FileField(null=True,blank=True)
	def __str__(self):
		k=self.house_idi
		return str(k)
#creating videos table in the database

class videotable(models.Model):
	house_idv=models.ForeignKey(House,on_delete=models.CASCADE)
	video=models.FileField(null=True,blank=True)
	def __str__(self):
		k=self.house_idv
		return str(k)
#creating farm table in the database

class FarmTable(models.Model):
	farm_id=models.IntegerField(primary_key=True)
	house_farm=models.ForeignKey(House,limit_choices_to={'isfarm':True},on_delete=models.CASCADE)
	area=models.FloatField()
	def __str__(self):
		k=self.farm_id
		return str(k)

#creating farmpoints table in the database

class farmpoints(models.Model):
	farm_idp=models.ForeignKey(FarmTable,on_delete=models.CASCADE)
	lat=models.FloatField()
	lon=models.FloatField()
	def __str__(self):
		k=self.farm_idp
		return str(k)

#creating farmcrop table in the database

class farmcroptable(models.Model):
	farm_idc=models.ForeignKey(FarmTable,on_delete=models.CASCADE)
	season_id=models.IntegerField()
	year=models.IntegerField()
	crop=models.CharField(max_length=35)
	def __str__(self):
		k=self.farm_idc
		return str(k)

#creating well table in the database

class welltable(models.Model):
	well_id=models.IntegerField(primary_key=True)
	farm_idw=models.ForeignKey(FarmTable,on_delete=models.CASCADE)
	lat=models.FloatField()
	lon=models.FloatField()
	depth=models.FloatField()
	def __str__(self):
		k=self.well_id
		return str(k)

#creating wellinformation table in the database

class wellinfo(models.Model):
	well_idf=models.ForeignKey(welltable,on_delete=models.CASCADE)
	yield1=models.FloatField()
	welldatetime=models.DateTimeField()
	def __str__(self):
		k=self.well_idf
		return str(k)

#creating farmcrop table in the database

class newfarmcroptable(models.Model):
        farm_idnc=models.ForeignKey(FarmTable,on_delete=models.CASCADE)
        season_id=models.IntegerField()
        year=models.IntegerField()
        crop=models.CharField(max_length=35)
        area=models.FloatField()
        def __str__(self):
                k=self.farm_idnc
                return str(k)

		







	

