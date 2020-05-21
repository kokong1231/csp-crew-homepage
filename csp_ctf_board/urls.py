from django.conf.urls import url, include

from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'csp_ctf_board'

urlpatterns = [
    url(r'^$', views.Csp_ctf_board.as_view(), name='csp_ctf_board'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)