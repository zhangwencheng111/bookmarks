from django.http import HttpResponse    
from django.shortcuts import render    
from django.contrib.auth import authenticate, login    
from account.form import LoginForm 
from django.contrib.auth.decorators import login_required


def login_user(request):
	"""用户登录"""
	if request.method != "POST":
		form = LoginForm()
		context = {"form": form}
		return render(request, "account/login.html", context)

	else:
		form = LoginForm(request.POST)
		if form.is_valid():
			tmp = form.cleaned_data
			#认证
			res = authenticate(username=tmp['username'], password=tmp["password"])
			#import pdb; pdb.set_trace()
			if res is not None:
				if res.is_active:
					login(request, res)
					return HttpResponse("login")
				else:
					return HttpResponse("no active")
			else:
				return HttpResponse('Invalid login')