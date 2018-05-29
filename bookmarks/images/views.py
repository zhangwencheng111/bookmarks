# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from django.shortcuts import get_object_or_404
from .models import Image


@login_required
def image_create(request):
	if request.method == "POST":
		form = ImageCreateForm(request.POST)
		if form.is_valid():
			new_form = form.save(commit=False)
			new_form.user = request.user
			new_form.save()
			return redirect(new_form.get_absolute_url())
	else:
		form = ImageCreateForm(data=request.GET)
		content = {"form": form, "section": "images"}
		return render(request, "images/image/create.html", content)


def image_detail(request, id, slug):
	detail_msg = get_object_or_404(Image, id=id, slug=slug)
	content = {"section": "images", "image": detail_msg}
	return render(request, "images/image/detail.html", content)