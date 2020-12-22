from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include
from .views import UserProfileView, TrackAddView


urlpatterns = [
    url(r'^', include('allauth.urls')),
    url(r'^profile$', UserProfileView.as_view(), name='profile'),
    url(r'^trackadd/$', TrackAddView.as_view(), name='track_add'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
