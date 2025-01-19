"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Definición de las rutas principales del proyecto
urlpatterns = [
    # Ruta para la interfaz de administración de Django
    path('admin/', admin.site.urls),
    # Rutas para la autenticación de usuarios (login, logout, password reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
    # Rutas para las URLs de la aplicación de blogs
    path('', include('blogs.urls')),
    # Rutas para las URLs de la aplicación de usuarios
    path('', include('users.urls')),
] 

# Añade la configuración para servir archivos estáticos en desarrollo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
