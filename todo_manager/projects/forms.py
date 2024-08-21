from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



from .models import Todo #............................


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        help_text=None,  # Remove help text for the password field
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        help_text=None,  # Remove help text for the password confirmation field
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
        help_texts = {
            'username': None,  # Remove or customize help text for the username field
        }







class TodoForm(forms.ModelForm): #.......................................
    class Meta:
        model = Todo
        fields = ['title', 'description', 'status']
