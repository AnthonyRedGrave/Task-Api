from django import forms
from .models import *
from django.contrib.auth.models import User


class UploadFileForm(forms.ModelForm):
    def clean(self):
        return self.cleaned_data

    class Meta:
        model = File
        fields = ['name', 'file', 'content', 'user']
        widgets = {'user': forms.HiddenInput()}


class RegForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget = forms.PasswordInput)
    phone = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['confirm_password'].label = 'Подтвердите пароль'
        self.fields['phone'].label = 'Телефон'
        self.fields['email'].label = 'Адрес электронной почты'

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError("Пользователь с таким адресом электронной почты уже существует!")

        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username = username).exists():
            raise forms.ValidationError('Пользователь с таким логином уже существует!')
        return username

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают!")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'first_name', 'last_name', 'email', 'phone']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not User.objects.filter(username = username).exists():
            raise forms.ValidationError('Пользователь с таким логином не существует!')

        user = User.objects.filter(username = username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Неверный пароль!')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']
