from ProjectDefence.accounts.models import Profile
from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import MinValueValidator

UserModel = get_user_model()


class SignUpForm(auth_forms.UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs=
            {'placeholder': "Enter your first name"}
        ),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs=
            {'placeholder': "Enter your last name"}
        ),
    )
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': "Enter your City/Town"}
        ),
    )
    street = forms.CharField(
        widget=forms.TextInput(
            attrs=
            {'placeholder': "Enter your Street name"}
        ),

    )
    number = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'placeholder': "Enter your House number"}
        ),
        validators=
        [MinValueValidator(1),
         ],
    )
    image = forms.URLField(
        widget=forms.URLInput(
            attrs=
            {'placeholder': "Add the URL for your profile picture"}
        ),
    )

    error_messages = {
        "password_mismatch": "One of the passwords is incorrect.",
    }

    class Meta:
        model = UserModel
        fields = (
            'first_name',
            'last_name',
            'city',
            'street',
            'number',
            'image',
            UserModel.USERNAME_FIELD,

        )
        field_classes = {
            'username': auth_forms.UsernameField,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password2"].help_text = None
        self.fields["password1"].help_text = None

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            user=user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            city=self.cleaned_data['city'],
            street=self.cleaned_data['street'],
            number=self.cleaned_data['number'],
            image=self.cleaned_data['image'],
        )

        if commit:
            profile.save()
        return user


class SignInForm(AuthenticationForm):
    email = forms.CharField()
    password = forms.CharField()


class ProfileFullfilForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = {
            'first_name',
            'last_name',
            'city',
            'number',
            'street',
            'image',
        }


class ProfileCheckForm(ProfileFullfilForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()
