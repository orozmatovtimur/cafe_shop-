from django import forms

from .models import *


class CreateDishForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class UpdateDishForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


# class ReviewForm(forms.ModelForm):
#     """Форма отзыва"""
#     captcha = ReCaptchaField()
#
#     class Meta:
#         model = Reviews
#         fields = ('name', 'email', 'text', 'captcha')
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control border'}),
#             'email': forms.EmailField(attrs={'class': 'form-control border'}),
#             'text': forms.Textarea(attrs={'class': 'form-control border'}),
#         }