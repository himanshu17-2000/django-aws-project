from django.shortcuts import render
from django.http import HttpResponse ,request
import json

# Create your views here.
def home_page(request):
    return HttpResponse(json.dumps({'message':"Himanshu's home page"}))