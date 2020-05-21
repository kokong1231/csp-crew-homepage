from . import views

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url

app_name = 'csp_main_home'

urlpatterns = [
    url(r'^$', views.Csp_main_home.as_view(), name='csp_main_home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)