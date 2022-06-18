from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from account.models import Account

class RegistrationForm(UserCreationForm):

    email = forms.EmailField(max_length=255, help_text='Required. Add a valid email address.')

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f'That email {email} is already in use.')

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f'That username {username} is already in use.')

class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

        def clean(self):
            if self.is_valid():
                email = self.cleaned_data['email']
                password = self.cleaned_data['password']
                if not authenticate(email=email, password=password):
                    raise forms.ValidationError('Invalid Login')

class EditProfileForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ('profile_image', 'fname', 'lname', 'bio')

    # def save(self, commit=True):
    #     account = super(EditProfileForm, self).save(commit=False)
    #     account.fname = self.cleaned_data['fname']
    #     account.lname = self.cleaned_data['lname']
    #     account.bio = self.cleaned_data['bio']
    #     account.profile_image = self.cleaned_data['profile_image']
    #     if commit:
    #         account.save()
    #     return account
