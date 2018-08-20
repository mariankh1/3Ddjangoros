from django.shortcuts import render
from mapbox import Directions
# Create your views here.

def default_maps(request):
	# TODO: move Token to settings.py file
	mapbox_access_token = 'pk.eyJ1IjoibWFyaWFua2giLCJhIjoiY2psMjQybDZiMW1lMjNwbnNjeG91OG4xeCJ9.bPbLuckWzOdT10hO5jUk8A'
	
	return render(request, 'details.html', {'mapbox_access_token':mapbox_access_token})
	
