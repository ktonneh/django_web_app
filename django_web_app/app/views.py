from django.shortcuts import render, HttpResponse
import requests
import json

# Create your views here.


def index(request):
	return HttpResponse('Hello you guy!!')


def test(request):
	return HttpResponse('Hello you guy, page 2 here##')

def profile(request):
	parsedData = []
	if request.method == "POST":
		jsonList = []
		req = requests.get('https://api.github.com/users/'+request.POST.get('user'))
		jsonList.append(json.loads(req.text))
	
		userData= {}
	
		for data in jsonList:
			userData['name'] = data['name']
			userData['blog'] = data['blog']
			userData['email'] = data['email']
			userData['public_gists'] = data['public_gists']
			userData['public_repos'] = data['public_repos']
			userData['avatar_url'] = data['avatar_url']
			userData['followers'] = data['followers']
			userData['following'] = data['following']

		parsedData.append(userData)
	return render(request,'app/profile.html',{'data':parsedData})

