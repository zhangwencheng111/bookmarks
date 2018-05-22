from django.http import HttpResponse    
from django.shortcuts import render    
from django.contrib.auth import authenticate, login, logout   
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .form import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib import messages


"""
def login_user(request):
    #用户登录
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
"""
from django.contrib.auth.decorators import login_required
@login_required
def dashboard(request):
    return render(request,
                 'account/dashboard.html',
                 {'section': 'dashboard'})


def log_out(request):
    logout(request)
    request.session.flush()
    #request.user = AnonymousUser
    # Redirect to a success page.
    return render(request, "account/logout.html")
    #return HttpResponseRedirect(reverse("sss"))


def register(request):
    if request.method == "POST":
        user_form  = UserRegistrationForm(request.POST)
        if user_form .is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form .save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            profile = Profile.objects.create(user=new_user)
            return render(request, "account/register_done.html", {"new_user":new_user})

    else:
        user_form = UserRegistrationForm()
        return render(request, "account/register.html", {"user_form":user_form})


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST) 
        profile_form = ProfileEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "Error updating your profile")
    else:
        user_form = UserEditForm(instance=request.user) 
        profile_form = ProfileEditForm(instance=request.user)

    return render(request, "account/edit.html", {"user_form":user_form, "profile_form":profile_form})
