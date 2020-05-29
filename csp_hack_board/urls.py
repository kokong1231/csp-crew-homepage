from django.conf.urls import url
from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'csp_hack_board'

urlpatterns = [
    url(r'^$', views.Csp_hack_board.as_view(), name='csp_hack_board'),
    url(r'^insert/$', views.check_post, name='csp_hack_insert'),
    path('<int:pk>/detail/', views.csp_hack_detail, name='csp_hack_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.Csp_hack_update.as_view(), name='csp_hack_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.Csp_hack_delete.as_view(), name='csp_hack_delete'),
    url(r'^nop/$', views.Nop.as_view(), name='nop'),

    #qna
    url(r'^qna/$', views.Csp_hack_board_qna.as_view(), name='csp_hack_board_qna'),
    url(r'^qna/insert/$', views.check_post_qna, name='csp_hack_insert_qna'),
    path('qna/<int:pk>/detail/', views.csp_hack_detail_qna, name='csp_hack_detail_qna'),
    url(r'^qna/(?P<pk>[0-9]+)/update/$', views.Csp_hack_update_qna.as_view(), name='csp_hack_update_qna'),
    url(r'^qna/(?P<pk>[0-9]+)/delete/$', views.Csp_hack_delete_qna.as_view(), name='csp_hack_delete_qna'),

    #comment
    path('<int:pk>/detail/comment/delete/<int:comment_id>/', views.comment_delete, name="comment_delete"),
    path('comment/update/<int:comment_id>/', views.comment_update, name="comment_update"),
    path('qna/<int:pk>/detail/comment/delete/<int:comment_id>/', views.comment_delete_qna, name="comment_delete_qna"),
    path('qna/comment/update/<int:comment_id>/', views.comment_update_qna, name="comment_update_qna"),

    #action
    path('close/', views.closed_page, name="closed_page")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)