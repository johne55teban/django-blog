from django.urls import path
from blogs import views

# Definimos el nombre del espacio de nombres para la aplicación 'blogs'
app_name = 'blogs'

# Lista de patrones de URL para la aplicación 'blogs'
urlpatterns = [
    # Ruta para la página de inicio, que utiliza la vista home_page
    path('', views.home_page),
    
    # Ruta para la vista de detalle de una publicación individual, identificada por un slug
    # Utiliza una vista basada en clases llamada PostView
    # El nombre de esta ruta es 'post'
    path('post/<slug:slug>', views.PostView.as_view(), name='post'),
    
    # Ruta para la vista de publicaciones destacadas
    # Utiliza una vista basada en clases llamada FeaturedListView
    # El nombre de esta ruta es 'featured'
    path('featured/', views.FeaturedListView.as_view(), name='featured'),
    
    # Ruta para la vista de publicaciones por categoría, identificada por un slug
    # Utiliza una vista basada en clases llamada CategoryListView
    # El nombre de esta ruta es 'category'
    path('category/<slug:slug>', views.CategoryListView.as_view(), name='category'),
    
    # Ruta para la vista de resultados de búsqueda
    # Utiliza una vista basada en clases llamada SearchResultsView
    # El nombre de esta ruta es 'search'
    path('search/', views.SearchResultsView.as_view(), name='search'),
]
