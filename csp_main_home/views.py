from django.shortcuts import render
# Create your views here.

from django.views import generic

class Csp_main_home(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        template_name = 'main_board.html'

        return render(request, template_name)