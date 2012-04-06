from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

import datetime

@login_required(login_url='/admin/')
def my_homepage_view(request):
    return HttpResponse("OTVA!")

@login_required(login_url='/admin/')
def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})