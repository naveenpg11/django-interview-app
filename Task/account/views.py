# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

# Create your views here.

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user/login')
        else:
        	return redirect('/user/register')
    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'reg_form.html', args)
