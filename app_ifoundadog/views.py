# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.views import generic

from app_ifoundadog import models
from . import account_helpers
from . import api_helpers
from .forms import *


class RedirectView(generic.RedirectView):
    permanent = False


class IndexPageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        return context

#class LogoutView(RedirectView):
#    url = '/'
#
#    def get_redirect_url(self, **kwargs):
#        logout(self.request)
#        return super(LogoutView, self).get_redirect_url(**kwargs)


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
        data = api_helpers.get_data()
        # quick one liner to just get the match
        match = [r for r in data['result'] if kwargs['id'] in r]

        # check if the data is in our database if not set to None because django
        try:
            dogprofile = models.UserProfile.objects.get(license_id=kwargs['id'])
        except models.UserProfile.DoesNotExist:
            dogprofile = None

        # if a match is found, and there's no profile create one
        if match and dogprofile is None:
            # turn neutered status to bool
            if str(match[0][6]).lower() == 'yes':
                neutered = True
            else:
                neutered = False
            # creates dog profile
            new_user = models.User.objects.create(
                username='DogOwner: ' + match[0][4],
                email='DogOwner: ' + match[0][4] + '@ifoundadog.net',
                first_name='DogOwner: ' + match[0][4],
                last_name='DogOwner: ' + match[0][4]
            )
            new_user.set_password(account_helpers.generate_password())
            new_user.save()
            dogprofile = models.UserProfile.objects.create(
                user=new_user,
                dog_name=match[0][4],
                first_name=new_user.first_name,
                last_name=new_user.last_name,
                owner_address=match[0][1],
                payment_date=match[0][2],
                years_issued=match[0][3],
                license_id=match[0][4],
                dog_sex_choices=match[0][5],
                neutered=neutered
            )
            dogprofile.save()
        #import pdb;
        #pdb.set_trace()
        context['dogprofile'] = dogprofile
        return context


# class LoginView(generic.FormView):
#     template_name = 'login.html'
#     form_class = LoginForm
#
#     def get_success_url(self):
#         user = self.request.POST['username']
#         password = self.request.POST['password']
#         authed_user = authenticate(
#             username=user,
#             password=password
#         )
#         login(request=self.request, user=authed_user)
#         user_id = models.User.objects.get(username=user).id
#         return '/'
