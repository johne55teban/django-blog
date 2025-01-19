from django.urls import reverse_lazy  # Importa reverse_lazy para generar URLs inversas de forma diferida
from django.views.generic.edit import FormView  # Importa la vista genérica FormView

from users.forms import RegisterForm  # Importa el formulario de registro de usuario definido en users.forms


class UserRegistration(FormView):
    """
    Vista para el registro de usuario.
    Utiliza la clase FormView para manejar la presentación del formulario y el procesamiento de datos.
    """

    template_name = 'users/registration.html'  # Plantilla utilizada para mostrar el formulario de registro
    form_class = RegisterForm  # Clase de formulario utilizada para el registro de usuario
    success_url = reverse_lazy('users:success')  # URL de redireccionamiento después de un registro exitoso

    def form_valid(self, form):
        """
        Método llamado cuando se envía un formulario válido.
        Guarda el formulario y devuelve una respuesta de éxito.
        """
        form.save()  # Guarda los datos del formulario
        return super(UserRegistration, self).form_valid(form)  # Devuelve una respuesta de éxito
