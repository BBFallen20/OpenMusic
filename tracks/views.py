from .models import Author, Tracks, Genre
from django.views.generic import DetailView, ListView


class TracksListView(ListView):
    model = Tracks
    template_name = 'tracks/track_list.html'

