from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Author, Track, Genre


class TrackListView(ListView):
    model = Track
    template_name = 'tracks/track_list.html'
    ordering = ['-title']


class TrackDetailView(DetailView):
    model = Track
    template_name = 'tracks/track_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Track, slug__iexact=self.kwargs['slug'])
