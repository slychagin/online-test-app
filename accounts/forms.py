from django import forms
from accounts.models import Account


class RegistrationForm(forms.ModelForm):
    """Create form for user registration"""
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Введите пароль'
        }
    ))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Повторите пароль'
        }
    ))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def __init__(self, *args, **kwargs):
        """Install css classes for all fields'"""
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Введите телефон'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        """
        Compare entered and repeat passwords.
        Raise validation error if passwords not equal
        """
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают!')