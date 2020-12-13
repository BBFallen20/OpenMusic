from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from .views import TrackDetailView, TrackListView


app_name = 'tracks'

urlpatterns = [
    url(r'^tracks/$', TrackListView.as_view(), name='tracks'),
    url(r'^track/(?P<slug>[-\w]+)/$', TrackDetailView.as_view(), name='track'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
