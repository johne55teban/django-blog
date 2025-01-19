from django import forms
# Importa las clases de formularios de Django

from blogs.models import Comment
# Importa el modelo Comment desde blogs.models

class PostCommentForm(forms.ModelForm):
    # Define un formulario de modelo para comentarios de publicaciones
    content = forms.CharField(label='Ingrese su comentario')
    # Campo para el contenido del comentario

    class Meta:
        # Clase Meta para definir los metadatos del formulario
        model = Comment
        # Asigna el modelo Comment al formulario
        fields = ['content']
        # Define los campos del formulario, en este caso, solo 'content'
