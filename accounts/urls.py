from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include


urlpatterns = [
    url(r'^', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
