from django import forms

class GuestLoginForm(forms.Form):
    display_name = forms.CharField(label='Display Name', max_length=100,
                                   widget=forms.TextInput(attrs={'placeholder': 'Enter your Display Name'}))

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100,
                               widget=forms.TextInput(attrs={'placeholder': 'Enter your Username'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Enter your Password'}))
