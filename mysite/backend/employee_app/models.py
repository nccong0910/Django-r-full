# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Info(models.Model):
    iduser = models.IntegerField(primary_key=True)
    adress = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'info'


class User(models.Model):
    iduser = models.AutoField(primary_key=True)
    nameuser = models.CharField(max_length=45)
    bd = models.DateField()

    class Meta:
        managed = False
        db_table = 'user'
