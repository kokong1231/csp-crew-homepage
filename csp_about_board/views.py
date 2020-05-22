from django.shortcuts import render

# Create your views here.

from django.views import generic

class Csp_about_board(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        template_name = 'csp_about_main.html'
        return render(request, template_name)