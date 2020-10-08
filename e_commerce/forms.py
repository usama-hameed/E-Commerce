from e_commerce.models import User,Products
from django import forms

class SignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password')

        widgets={
            'password':forms.PasswordInput()
        }

class AddProductForm(forms.ModelForm):
    class Meta:
        model=Products
        fields=('name','price')  