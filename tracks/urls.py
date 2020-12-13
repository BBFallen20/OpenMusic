from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


app_name = 'tracks'

urlpatterns = [
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
