from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView, CreateView
from .models import Author, Track


class TrackListView(ListView):
    model = Track
    template_name = 'tracks/track_list.html'
    paginate_by = 5

    def get_queryset(self):
        genre = self.kwargs.get('genre', None)
        if genre:
            return Track.objects.filter(genre__name=genre)
        else:
            return Track.objects.all()


class TrackDetailView(DetailView):
    model = Track
    template_name = 'tracks/track_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Track, slug__iexact=self.kwargs['slug'])


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'tracks/author_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Author, slug__iexact=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Tracks'] = Track.objects.filter(author__slug=self.kwargs['slug'])
        return context


class MainView(TemplateView):
    template_name = 'index.html'

