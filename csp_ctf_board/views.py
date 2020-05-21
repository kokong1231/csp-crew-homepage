from django.shortcuts import render

# Create your views here.

from django.views import generic

class Csp_ctf_board(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        template_name = 'ctf_board.html'
        return render(request, template_name)