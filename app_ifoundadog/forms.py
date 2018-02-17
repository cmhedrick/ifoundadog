from django import forms

from app_ifoundadog import models
from . import account_helpers
from . import api_helpers

# keep the below code just in case.
# class AddUserForm(forms.Form):
#     email = forms.EmailField(
#         widget=forms.TextInput(attrs={
#             'placeholder': "Email Address"
#         }),
#         label="Email"
#     )
#     password1 = forms.CharField(
#         widget = forms.PasswordInput(attrs={
#             'placeholder' : "Password",
#         }),
#         max_length=100,
#         label = "Password"
#     )
#     password2 = forms.CharField(
#         widget = forms.PasswordInput(attrs={
#             'placeholder' : "Confirm Password",
#         }),
#         max_length=100,
#         label = "Password Confirm"
#     )
#     first_name = forms.CharField(
#         widget=forms.TextInput(attrs={
#             'placeholder': "Owner's First Name"
#         }),
#         label="First Name"
#     )
#     last_name = forms.CharField(
#         widget=forms.TextInput(attrs={
#             'placeholder': "Owner's Last Name"
#         }),
#         label="Last Name"
#     )
#     dog_name = forms.CharField(
#         widget=forms.TextInput(attrs={
#             'placeholder': "Dog's Name"
#         }),
#         label="Dog's Name"
#     )
#     profile_pic = forms.ImageField(required=False)
#
#     def __init__(self, *args, **kwargs):
#         super(AddUserForm, self).__init__(*args, **kwargs)
#
#     def clean_password2(self):
#         pwd1 = self.cleaned_data["password1"]
#         pwd2 = self.cleaned_data["password2"]
#         if pwd1 != pwd2:
#             raise forms.ValidationError("The two passwords don't match.")
#         return pwd2
#
#     def clean_profile_pic(self):
#         profile_pic = self.cleaned_data['profile_pic']
#         return profile_pic
#
#     def save(self):
#         info = self.cleaned_data
#         new_user = models.User.objects.create(
#             username=info['username'],
#             email=info['email'],
#             first_name=info['first_name'],
#             last_name=info['last_name']
#         )
#         new_user.set_password(info['password1'])
#         new_user.save()
#         new_pro = models.UserProfile.objects.create(
#             user=new_user,
#             dog_name=info['dog_name'],
#             profile_pic=info['profile_pic']
#         )
#         new_pro.save()


class LookUpLicenseForm(forms.Form):
    inputLicense = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': "Dog Licence",
            'class': "form-control"
        }),
        label="Dog License"
    )

    def __init__(self, *args, **kwargs):
        super(LookUpLicenseForm, self).__init__(*args, **kwargs)

    def clean(self):
        """
        provides validation for form after submission
        :return:
        """
        cleaned_data = super(LookUpLicenseForm, self).clean()
        licence = str(cleaned_data.get('inputLicense')).upper()
        if licence is None or str(licence).strip() == '':
            self.add_error('inputLicense', 'No licence provided.')
        if len(str(licence).strip()) != 7:
            self.add_error(
                'inputLicense', 'Licences must contain 7 characters!'
            )

        # check if the data is in our database if not set to None because django
        try:
            dogprofile = models.UserProfile.objects.get(license_id=licence)
            match = None
        except models.UserProfile.DoesNotExist:
            dogprofile = None

        # if profile is not in the db, check the open data portal
        if dogprofile is None:
            data = api_helpers.get_data()
            # quick one liner to just get the match
            match = [r for r in data['result'] if licence in r]

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

        elif not match and dogprofile is None:
            self.add_error(
                'inputLicense', 'No dog has this ID!'
            )

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': "Username",
            'class': "form-control"
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': "Password",
            'class': "form-control"
        }),
        label="Password"
    )
