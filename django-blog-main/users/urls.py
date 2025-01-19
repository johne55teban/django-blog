from django.urls import path
from django.views.generic import TemplateView  # Importa la vista genérica TemplateView

from users import views  # Importa las vistas definidas en la aplicación de usuarios

app_name = 'users'  # Define el espacio de nombres de la aplicación de usuarios

urlpatterns = [
    # Ruta para la vista de registro de usuario
    path('registraion/', views.UserRegistration.as_view(), name='registration'),
    
    # Ruta para la vista de éxito de registro de usuario, utiliza TemplateView
    path('success/', TemplateView.as_view(template_name='users/success_registration.html'), name='success')
]
