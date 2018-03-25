# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import TemplateView
from django.views import generic

from app_ifoundadog import models

from .forms import *


class RedirectView(generic.RedirectView):
    permanent = False


class IndexPageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        return context


class LogoutView(RedirectView):
    url = '/'

    def get_redirect_url(self, **kwargs):
        logout(self.request)
        return super(LogoutView, self).get_redirect_url(**kwargs)


class LicenseLookUpView(generic.FormView):
    template_name = 'index.html'
    form_class = LookUpLicenseForm

    def get_context_data(self, *args, **kwargs):
        context = super(LicenseLookUpView, self).get_context_data(
            *args, **kwargs
        )
        context['kwargs'] = self.kwargs
        context['request'] = self.request
        return context

    def get_form_kwargs(self):
        kwargs = super(LicenseLookUpView, self).get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        #form.save()
        return super(LicenseLookUpView, self).form_valid(form)

    def get_success_url(self):
        return '/dog/' + str(self.request.POST['inputLicense']).upper()


class DogDetailView(generic.TemplateView):
    template_name = "dog_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DogDetailView, self).get_context_data(**kwargs)
        # check if the data is in our database if not set to None because django
        try:
            dogprofile = models.UserDogProfile.objects.get(license_id=kwargs['id'])
            context['dogprofile'] = dogprofile
            context['user'] = self.request.user
        except models.UserDogProfile.DoesNotExist:
            dogprofile = None

        return context


class LoginView(generic.FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def get_success_url(self):
        user = self.request.POST['username']
        password = self.request.POST['password']
        authed_user = authenticate(
            request=self.request, username=user, password=password
        )
        login(request=self.request, user=authed_user)

        return '/'
