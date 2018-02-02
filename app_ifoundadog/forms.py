from django import forms

#from app_ifoundadog import models

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
        licence = cleaned_data.get('inputLicense')
        if licence is None or str(licence).strip() == '':
            self.add_error('inputLicense', 'No licence provided.')
        if len(str(licence).strip()) != 7:
            self.add_error('inputLicense', 'Licences must contain 7 characters!')
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
