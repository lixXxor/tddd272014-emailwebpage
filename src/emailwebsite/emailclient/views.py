from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from social.backends.google import GooglePlusAuth
from social.apps.django_app.default.models import UserSocialAuth

from django.utils import simplejson

import json
import ast

from emailclient.models import emailclient
import emailclient.emailService
# Create your views here.

def login(request):

	plus_scope = ' '.join(settings.SOCIAL_AUTH_GOOGLE_PLUS_SCOPE)
	#plus_scope = ' '.join(GooglePlusAuth.DEFAULT_SCOPE)
	context = {
			   'plus_scope': plus_scope,
			   'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None)}
	return render(request, 'emailclient/login.html', context)

def index(request):
	instance = UserSocialAuth.objects.get(user=request.user, provider='google-plus')
	token = list(request.user.social_auth.values_list('extra_data'))
	usableToken = json.loads(eval(str(token).replace('[(', '').replace(',)]', '')))


	userEmail = request.user.email
	LAST_EMAIL = emailclient.emailService.getMail(userEmail, usableToken.get('access_token'))
	
	plus_scope = ' '.join(GooglePlusAuth.DEFAULT_SCOPE)
	context = {
			'token'	: simplejson.dumps(token),
			'plus_scope': plus_scope,
			'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None),
			'last_email': json.dumps(LAST_EMAIL)
	}	
	return render(request, 'emailclient/index.html', context)

@login_required
def email(request):
	instance = UserSocialAuth.objects.get(user=request.user, provider='google-plus')
	token = request.user.social_auth.values_list('extra_data')
	context = {
			'token'	: token
	}	
	return render(request, 'emailclient/email.html', context)


def sendMail(request):
	to = request.GET.get('to')
	subject = request.GET.get('subject')
	message = request.GET.get('message')
	token = request.GET.get('access_token')
	emailclient.emailService.sendMail(request.user.email, token,to, subject, message)
	#emailclient.emailService.getMail(request.user.email, token)
	
	return email(request)

def send(request):
	return render(request, 'emailclient/send.html', None)


def test(request):
	print(request.user.email)
	return render(request, 'emailclient/test.html', None)

def logout(request):
	auth_logout(request)
	context = {'loggedOut': True}
	return render(request, 'emailclient/logout.html', context)





