from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.contrib.gis.geos import *
from django.core import serializers
import re

from app.models import *

@csrf_exempt
# Create your views here.
def index(request):
	return render_to_response('index.html')

@csrf_exempt
def networks(request):
	if request.method == 'POST':
		data = simplejson.loads(request.body)	
		network = Network(name=data.get('name'), company=data.get('company'), mode=data.get('mode'), geom=fromstr('POINT({0} {1})'.format(data.get('geom')[0], data.get('geom')[1]), srid=4326))
		network.save()
		return HttpResponse("OK")
	else:
		all_networks = Network.objects.all()
		data = serializers.serialize("json", all_networks)
		return HttpResponse(data, content_type="application/json")

@csrf_exempt
def routes(request):
	if request.method == 'POST':
		data = simplejson.loads(request.body)
		geomStr = ""
		for latlng in data.get('geom'):
			geomStr += str(latlng[0]) + " " + str(latlng[1]) + ", "
		geomStr = geomStr[:-2]
		print geomStr
		route = Route(name=data.get('name'), description=data.get('description'), geom=fromstr('MULTILINESTRING(({0}))'.format(geomStr)))
		route.network_id = data.get('network')
		route.save()
		return HttpResponse("OK")	
	else:
		net_id = request.GET.get('network_id')
		routes = Route.objects.filter(network_id=net_id)
		data = serializers.serialize("json", routes)
		return HttpResponse(data, content_type="application/json")