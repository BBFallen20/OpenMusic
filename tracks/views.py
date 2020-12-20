from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Author, Track, Genre


class TrackListView(ListView):
    model = Track
    template_name = 'tracks/track_list.html'


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
