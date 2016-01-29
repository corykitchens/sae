from django import forms


class LoginUserForm(forms.Form):
	username = forms.CharField(label="username", max_length=100)
	password = forms.CharField(label="password", max_length=30, widget=forms.PasswordInput)