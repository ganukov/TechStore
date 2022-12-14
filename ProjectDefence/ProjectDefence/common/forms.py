from ProjectDefence.accounts.models import Profile
from django import forms
from django.contrib.auth import get_user_model

UserModel = get_user_model()


# class ChangeDetailsForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = (
#             'first_name',
#             'last_name',
#             'city',
#             'street',
#         )


class ContactForm(forms.Form):
    first_name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.Textarea()
