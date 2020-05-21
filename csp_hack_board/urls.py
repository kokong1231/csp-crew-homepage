from django.conf.urls import url

from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'csp_hack_board'

urlpatterns = [
    url(r'^$', views.Csp_hack_board.as_view(), name='csp_hack_board'),
    url(r'^insert/$', views.check_post, name='csp_hack_insert'),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.Csp_hack_detail.as_view(), name='csp_hack_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.Csp_hack_update.as_view(), name='csp_hack_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.Csp_hack_delete.as_view(), name='csp_hack_delete'),
    url(r'^nop/$', views.Nop.as_view(), name='nop'),

    #qna
    url(r'^qna/$', views.Csp_hack_board_qna.as_view(), name='csp_hack_board_qna'),
    url(r'^qna/insert/$', views.check_post_qna, name='csp_hack_insert_qna'),
    url(r'^qna/(?P<pk>[0-9]+)/detail/$', views.Csp_hack_detail_qna.as_view(), name='csp_hack_detail_qna'),
    url(r'^qna/(?P<pk>[0-9]+)/update/$', views.Csp_hack_update_qna.as_view(), name='csp_hack_update_qna'),
    url(r'^qna/(?P<pk>[0-9]+)/delete/$', views.Csp_hack_delete_qna.as_view(), name='csp_hack_delete_qna'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)