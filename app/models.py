from django.contrib.gis.db import models

# Create your models here.
class Network(models.Model):
	name = models.CharField(max_length=500)
	company = models.CharField(max_length=500)
	mode = models.IntegerField()
	geom = models.PointField()

class Route(models.Model):
	network = models.ForeignKey(Network)
	name = models.CharField(max_length=500)
	description = models.CharField(max_length=500)
	geom = models.MultiLineStringField()

class Stop(models.Model):
	route = models.ForeignKey(Route)
	name = models.CharField(max_length=500)
	segment_num = models.IntegerField()
	segment_offset = models.FloatField()
	is_origin = models.BooleanField()
	is_destination = models.BooleanField()
	geom = models.PointField()

class Schedule(models.Model):
	stop = models.ForeignKey(Stop, related_name='schedule_stop')
	towards = models.ForeignKey(Stop, related_name='schedule_dest')
	arrival_time = models.DateField()
	departure_time = models.DateField()


class User(models.Model):
	name = models.CharField(max_length=500)
	email = models.CharField(max_length=500)
	can_edit = models.BooleanField()