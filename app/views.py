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
		pass
	else:
		network_id = request.GET.get('network_id')
		pass
	return HttpResponse("OK")