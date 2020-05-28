from django.conf.urls import url
from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'csp_prog_board'

urlpatterns = [
    url(r'^$', views.Csp_prog_board.as_view(), name='csp_prog_board'),
    url(r'^insert/$', views.check_post, name='csp_prog_insert'),
    path('<int:pk>/detail/', views.csp_prog_detail, name='csp_prog_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.Csp_prog_update.as_view(), name='csp_prog_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.Csp_prog_delete.as_view(), name='csp_prog_delete'),
    url(r'^nop/$', views.Nop.as_view(), name='nop'),

    # QnA
    url(r'^qna/$', views.Csp_prog_board_qna.as_view(), name='csp_prog_board_qna'),
    url(r'^qna/insert/$', views.check_post_qna, name='csp_prog_insert_qna'),
    path('qna/<int:pk>/detail/', views.csp_prog_detail_qna, name='csp_prog_detail_qna'),
    url(r'^qna/(?P<pk>[0-9]+)/update/$', views.Csp_prog_update_qna.as_view(), name='csp_prog_update_qna'),
    url(r'^qna/(?P<pk>[0-9]+)/delete/$', views.Csp_prog_delete_qna.as_view(), name='csp_prog_delete_qna'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)