from django.shortcuts import render
import json
from django.http import HttpResponse , HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

def home(request):
	pass

@csrf_exempt
def loginController(request):
	post_data = request.body
	user_id = post_data["user"]
	pass_key = post_data["password"]
	result = dict()
	try:
		user_profile_get = UserProfile.objects.get(user = user_id, password = pass_key)
		if user_profile_get :
			result["result"] = "SUCCESS"
			result["status"] = 200
			result["exception"] = "none"
			return HttpResponse(json.dumps(result), content_type = "application/json")
	
	except Exception as e:
		print "error encountered! "
		print e
		result["result"] = "FAILURE"
		result["status"] = 500
		result["exception"] = e
		return HttpResponse(json.dumps(result), content_type = "application/json")


