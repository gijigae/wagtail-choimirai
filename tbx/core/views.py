import requests

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
#import json


def error404(request):
    if '/play/' in request.path:
        return render(request, 'play_404.html', {'play_404': True},  status=404)
    else:
        return render(request, '404.html', status=404)


def newsletter_subsribe(request):
    if request.is_ajax() and request.GET.get('email'):
        requests.post(
            "https://us3.api.mailchimp.com/3.0/lists/3d650ffa14/members",
            auth=('apikey', settings.MAILCHIMP_KEY),
            json={
                  #'id': settings.MAILING_LIST_ID,
                  'data':{'email_address': request.GET.get('email')}}
        )
    return HttpResponse()
