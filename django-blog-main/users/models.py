from django.contrib.auth.models import AbstractUser  # Importa el modelo AbstractUser de Django

class User(AbstractUser):
    # Este modelo extiende el modelo AbstractUser

    def __str__(self):
        # Define el método __str__ para representar un objeto de usuario como una cadena
        return f'{self.last_name}, {self.first_name}'  # Retorna el nombre completo del usuario
