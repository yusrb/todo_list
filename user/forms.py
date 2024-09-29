from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class CustomLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'border border-blue-300 rounded-md p-2 focus:border-blue-500 focus:ring focus:ring-blue-200',
            'placeholder': 'Username'
        }),
        label='Username'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'border border-blue-300 rounded-md p-2 focus:border-blue-500 focus:ring focus:ring-blue-200',
            'placeholder': 'Password'
        }),
        label='Password'
    )

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.user = None

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        self.user = authenticate(self.request, username=username, password=password)

        if self.user is None:
            raise forms.ValidationError("Username atau password salah.")

        return cleaned_data

    def get_user(self):
        return self.user 

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'border border-blue-300 rounded-md p-2 focus:border-blue-500 focus:ring focus:ring-blue-200'
            })
