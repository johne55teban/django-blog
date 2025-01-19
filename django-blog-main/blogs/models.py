from django.db import models
# Importa las clases de modelos de Django
from django.conf import settings
# Importa la configuración del proyecto
from django.urls import reverse
# Importa las funciones para la creación de URLs
from django.utils import timezone
# Importa la zona horaria de Django

# Modelo para las publicaciones
class Post(models.Model):
    title = models.CharField(max_length=255)
    # Título de la publicación
    slug = models.SlugField(unique=True)
    # Slug único para la URL
    overview = models.TextField()
    # Resumen de la publicación
    date_created = models.DateTimeField(auto_now_add=True)
    # Fecha de creación de la publicación
    content = models.TextField()
    # Contenido de la publicación
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    # Autor de la publicación
    categories = models.ManyToManyField('Category')
    # Categorías a las que pertenece la publicación
    featured = models.BooleanField(default=False)
    # Publicación destacada
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    # Imagen asociada a la publicación
    pub_date = models.DateTimeField(default=timezone.now)
    # Fecha de publicación

    def get_absolute_url(self):
        # Método para obtener la URL absoluta de la publicación
        return reverse("blogs:post", kwargs={"slug": self.slug})

    class Meta:
        # Metadatos del modelo
        ordering = ["-date_created"]
        # Ordenar las publicaciones por fecha de creación descendente
    
    def __str__(self):
        # Método para devolver una representación legible de la instancia
        return self.title


# Modelo para las categorías
class Category(models.Model):
    title = models.CharField(max_length=255)
    # Título de la categoría
    slug = models.SlugField(unique=True)
    # Slug único para la URL

    class Meta:
        # Metadatos del modelo
        verbose_name_plural = 'categories'
        # Nombre en plural de la categoría

    def get_absolute_url(self):
        # Método para obtener la URL absoluta de la categoría
        return reverse("blogs:category", kwargs={"slug": self.slug})

    def __str__(self):
        # Método para devolver una representación legible de la instancia
        return self.title


# Modelo para los comentarios de las publicaciones
class Comment(models.Model):
    content = models.TextField(max_length=1000, help_text='Ingrese un comentario')
    # Contenido del comentario
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    # Autor del comentario
    post_date = models.DateTimeField(auto_now_add=True)
    # Fecha de publicación del comentario
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # Publicación a la que pertenece el comentario

    class Meta:
        # Metadatos del modelo
        ordering = ['-post_date']
        # Ordenar los comentarios por fecha de publicación descendente

    def __str__(self):
        # Método para devolver una representación legible de la instancia
        len_title = 15
        if len(self.content) > len_title:
            return self.content[:len_title] + '...'
        return self.content
