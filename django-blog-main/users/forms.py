from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ocultar los comentarios de ayuda para los requisitos de la contraseña
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        # Ocultar el comentario de ayuda para el campo username
        self.fields['username'].help_text = None

    class Meta:
        model = get_user_model()
        fields = ("username", "", "password1", "password2")
