from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# User = get_user_model()


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('User with such email already exists.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Such username already exists.')
        return username


    def clean_password(self):
        if not self.cleaned_data['password1']:
            raise forms.ValidationError("Enter a password.")
        return self.cleaned_data['password1']

    def clean_password2(self):
        if not self.cleaned_data['password2']:
            raise forms.ValidationError("Enter a password.")
        return self.cleaned_data['password2']

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user





