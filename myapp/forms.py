from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

def validate_email(value):
  if User.objects.filter(email = value).exists():
    raise ValidationError(f"A user with this email already exists.")

class RegisterationForm(UserCreationForm):
  password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
  password2 = forms.CharField(label="Confirm Password (again)", widget=forms.PasswordInput(attrs={'class':'form-control'}))
  username = forms.CharField(label="User Name", label_suffix="", widget=forms.TextInput(attrs={'class':'form-control'}))
  email = forms.CharField(validators = [validate_email], label="Email Id", label_suffix="", widget=forms.EmailInput(attrs={'class':'form-control'}))

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, "class": "form-control"}))
    password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class": "form-control"}),
    )
    class Meta:
      model = User
      fields = ['username', 'password']

class ProfileChangeForm(forms.ModelForm):
  username = forms.CharField(label="User Name", label_suffix="", widget=forms.TextInput(attrs={'class':'form-control'}))
  first_name = forms.CharField(label="First Name", label_suffix="", widget=forms.TextInput(attrs={'class':'form-control'}))
  last_name = forms.CharField(label="Last Name", label_suffix="", widget=forms.TextInput(attrs={'class':'form-control'}))
  email = forms.CharField(label="Email Id", label_suffix="", widget=forms.EmailInput(attrs={'class':'form-control'}))
  
  class Meta:
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']

class EmailValidationOnForgotPassword(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={"autocomplete": "email", "class":"form-control"}),)
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = _("There is no user registered with the specified email address.")
            self.add_error('email', msg)
        return email

class ReSetPasswordForm(SetPasswordForm):
  new_password1 = forms.CharField(label=_("New password"), widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class":"form-control"}), strip=False)
  new_password2 = forms.CharField(label=_("New password confirmation"), strip=False, widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class":"form-control"}))