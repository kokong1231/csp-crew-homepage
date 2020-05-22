"""CSP_CREW_HOMEPAGE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('csp_on/', admin.site.urls),
    path('main/', include('csp_main_home.urls')),
    path('', include('csp_main_home.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # board
    path('hackboard/', include('csp_hack_board.urls')),
    path('progboard/', include('csp_prog_board.urls')),
    path('ctfboard/', include('csp_ctf_board.urls')),
    path('aboutboard/', include('csp_about_board.urls')),

    # account
    path('sign_c/', include('account.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)