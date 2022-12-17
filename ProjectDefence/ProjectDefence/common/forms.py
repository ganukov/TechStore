from ProjectDefence.accounts.models import Profile
from django import forms
from django.contrib.auth import get_user_model

from ProjectDefence.common.models import Complaint

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


class ContactForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = (
            'first_name',
            'email',
            'subject',
            'message',
        )
