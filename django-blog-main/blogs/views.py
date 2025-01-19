from django.shortcuts import render
from django.views import generic, View
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.db.models import Q
from django.urls import reverse

from blogs.models import Post, Category
from blogs.forms import PostCommentForm

# Vista para la página de inicio
def home_page(request):
    # Filtra las publicaciones cuyo pub_date es menor o igual a la fecha actual
    posts = Post.objects.filter(pub_date__lte=timezone.now())
    # Filtra las publicaciones destacadas cuyo pub_date es menor o igual a la fecha actual
    featured = Post.objects.filter(featured=True).filter(pub_date__lte=timezone.now())[:3]

    context = {
        'post_list': posts,  # Lista de publicaciones a pasar al template
        'featured': featured  # Lista de publicaciones destacadas a pasar al template
    }

    return render(request, 'blogs/home_page.html', context=context)

# Vista para el detalle de una publicación
class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.filter(pub_date__lte=timezone.now())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostCommentForm()  # Formulario de comentario a pasar al template
        return context

# Vista para manejar el formulario de comentarios de publicaciones
class PostCommentFormView(LoginRequiredMixin, SingleObjectMixin, FormView):
    template_name = 'blogs/post_detail.html'
    form_class = PostCommentForm
    model = Post

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        f = form.save(commit=False)
        f.author = self.request.user  # Asigna el autor del comentario como el usuario actual
        f.post = self.object  # Asigna el post relacionado al comentario
        f.save()
        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse('blogs:post', kwargs={'slug': self.object.slug}) + '#comments-section'

# Vista para manejar las solicitudes GET y POST de una publicación
class PostView(View):
    def get(self, request, *args, **kwargs):
        view = PostDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostCommentFormView.as_view()
        return view(request, *args, **kwargs)

# Vista para mostrar una lista de publicaciones destacadas
class FeaturedListView(generic.ListView):
    model = Post
    template_name = 'blogs/results.html'
    paginate_by = 2

    def get_queryset(self):
        query = Post.objects.filter(featured=True).filter(pub_date__lte=timezone.now())
        return query

# Vista para mostrar las publicaciones de una categoría específica
class CategoryListView(generic.ListView):
    model = Post
    template_name = 'blogs/results.html'
    paginate_by = 2

    def get_queryset(self):
        query = self.request.path.replace('/category/', '')
        print(query)
        post_list = Post.objects.filter(categories__slug=query).filter(pub_date__lte=timezone.now())
        return post_list

# Vista para mostrar los resultados de búsqueda
class SearchResultsView(generic.ListView):
    model = Post
    template_name = 'blogs/results.html'
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('search')
        post_list = Post.objects.filter(
            Q(title__icontains=query) | Q(categories__title__icontains=query)
        ).filter(pub_date__lte=timezone.now()).distinct()
        return post_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('search')  # Incluye la consulta de búsqueda en el contexto
        return context
