from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

# @login_required()
def alogin(request):

    errors = False

    if request.user.is_authenticated():
        return redirect(reverse('menu', kwargs={}))

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect(reverse('menu', kwargs={}))
        else:
            errors = True

    return render(request, "login.html", {'errors': errors})

@login_required()
def menu(request):
    return render(request, "menu.html", {})