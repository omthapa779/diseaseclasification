from django import forms
from classification.models import User  # Make sure to import your User model if you have one.

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User  # Replace with your actual model name if different.
        fields = ['username', 'email', 'password']  # Adjust fields as necessary.
