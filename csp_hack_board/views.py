from django.shortcuts import render, get_object_or_404, reverse
from .models import Csp_hack_list, Csp_hack_list_qna
from .forms import Csp_hack_form, Csp_hack_form_qna

# Create your views here.

from django.views import generic
from django.core.paginator import Paginator
from django.views.generic.edit import FormMixin


class Csp_hack_board(generic.TemplateView):

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated == False:
            return render(self.request, 'nop.html', {"message": "Nop! Login First."})

        elif request.user.last_name != 'hack' and request.user.last_name != 'admin':
            return render(self.request, 'nop.html', {"message": "Nop! You are not hacking member!"})

        template_name = 'hack_board.html'
        csp_hack_page = Csp_hack_list.objects
        hack_page_list = Csp_hack_list.objects.all().order_by('-no')
        paginator = Paginator(hack_page_list, 10)
        page = request.GET.get('page')
        posts = paginator.get_page(page)

        return render(request, template_name, {'csp_hack_page': csp_hack_page, 'posts': posts, 'top': hack_page_list})

class Csp_hack_detail(generic.DetailView):

    model = Csp_hack_list
    template_name = 'csp_hack_detail.html'
    context_object_name = 'csp_hack_list'

class Csp_hack_update(generic.UpdateView):

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated == False:
            return render(self.request, 'nop.html', {"message": "Nop! Login First."})

        elif request.user.last_name != 'hack' and request.user.last_name != 'admin':
            return render(self.request, 'nop.html', {"message": "Nop! You are not hacking member!"})

    model = Csp_hack_list
    fields = ('title', 'content', 'is_complete')
    template_name = 'csp_hack_update.html'
    success_url = '/hackboard/'

    def form_valid(self, form):
        form.save()
        return render(self.request, 'csp_hack_success.html', {"message": "Update Success!"})

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

class Csp_hack_delete(generic.DeleteView):
    model = Csp_hack_list
    success_url = '/hackboard/'
    context_object_name = 'csp_hack_list'

class Nop(generic.TemplateView):

    def check_post(self, request):

        template_name = 'nop.html'
        message = "Nop! Login First."

        return render(request, template_name, {"message":message})

def check_post(request):

    template_name = 'csp_hack_success.html'

    if request.method == "POST":
        form = Csp_hack_form(request.POST)
        if form.is_valid():
            hack = form.save(commit=False)
            hack.user_id = request.user.first_name
            hack.user_name = request.user.username
            hack.csp_hack_save()
            message = "Success!"
            return render(request, template_name, {"message":message})

    else:
        template_name = 'csp_hack_insert.html'
        form = Csp_hack_form
        return render(request, template_name, {"form" : form})

    # QNA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # QNA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Csp_hack_board_qna(generic.TemplateView):

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated == False:
            return render(self.request, 'nop.html', {"message": "Nop! Login First."})

        elif request.user.last_name != 'hack' and request.user.last_name != 'admin':
            return render(self.request, 'nop.html', {"message": "Nop! You are not hacking member!"})

        template_name = 'hack_board_qna.html'
        csp_hack_qna = Csp_hack_list_qna.objects
        hack_page_qna = Csp_hack_list_qna.objects.all().order_by('-no')
        paginator = Paginator(hack_page_qna, 10)
        page = request.GET.get('page')
        posts = paginator.get_page(page)

        return render(request, template_name, {'csp_hack_qna': csp_hack_qna, 'posts': posts, 'top': hack_page_qna})

class Csp_hack_detail_qna(generic.DetailView):

    model = Csp_hack_list_qna
    template_name = 'csp_hack_detail_qna.html'
    context_object_name = 'csp_hack_list_qna'

class Csp_hack_update_qna(generic.UpdateView):

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated == False:
            return render(self.request, 'nop.html', {"message": "Nop! Login First."})

        elif request.user.last_name != 'hack' and request.user.last_name != 'admin':
            return render(self.request, 'nop.html', {"message": "Nop! You are not hacking member!"})

    model = Csp_hack_list_qna
    fields = ('title', 'content', 'is_complete')
    template_name = 'csp_hack_update_qna.html'
    success_url = '/hackboard/qna/'

    def form_valid(self, form):
        form.save()
        return render(self.request, 'csp_hack_success_qna.html', {"message": "Update Success!"})

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

class Csp_hack_delete_qna(generic.DeleteView):
    model = Csp_hack_list_qna
    success_url = '/hackboard/qna/'
    context_object_name = 'csp_hack_list_qna'

def check_post_qna(request):

    template_name = 'csp_hack_success_qna.html'

    if request.method == "POST":
        form = Csp_hack_form_qna(request.POST)
        if form.is_valid():
            hack = form.save(commit=False)
            hack.user_id = request.user.first_name
            hack.user_name = request.user.username
            hack.csp_hack_save_qna()
            message = "Success!"
            return render(request, template_name, {"message":message})

    else:
        template_name = 'csp_hack_insert_qna.html'
        form = Csp_hack_form_qna
        return render(request, template_name, {"form" : form})
