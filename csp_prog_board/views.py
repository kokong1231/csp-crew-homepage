from django.shortcuts import render
from .models import Csp_prog_list, Csp_prog_list_qna
from .forms import Csp_prog_form, Csp_prog_form_qna

# Create your views here.

from django.views import generic
from django.core.paginator import Paginator


class Csp_prog_board(generic.TemplateView):

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated == False:
            return render(self.request, 'nop.html', {"message": "Nop! Login First."})

        elif request.user.last_name != 'prog' and request.user.last_name != 'admin':
            return render(self.request, 'nop.html', {"message": "Nop! You are not programming member!"})

        template_name = 'prog_board.html'
        csp_prog_page = Csp_prog_list.objects
        prog_page_list = Csp_prog_list.objects.all().order_by('-no')
        paginator = Paginator(prog_page_list, 10)
        page = request.GET.get('page')
        posts = paginator.get_page(page)

        return render(request, template_name, {'csp_prog_page': csp_prog_page, 'posts': posts, 'top': prog_page_list})

class Csp_prog_detail(generic.DetailView):

    model = Csp_prog_list
    template_name = 'csp_prog_detail.html'
    context_object_name = 'csp_prog_list'

class Csp_prog_update(generic.UpdateView):

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated == False:
            return render(self.request, 'nop.html', {"message": "Nop! Login First."})

        elif request.user.last_name != 'prog' and request.user.last_name != 'admin':
            return render(self.request, 'nop.html', {"message": "Nop! You are not programming member!"})

    model = Csp_prog_list
    fields = ('title', 'content', 'is_complete')
    template_name = 'csp_prog_update.html'
    success_url = '/progboard/'

    def form_valid(self, form):
        form.save()
        return render(self.request, 'csp_prog_success.html', {"message": "Update Success!"})

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

class Csp_prog_delete(generic.DeleteView):
    model = Csp_prog_list
    success_url = '/progboard/'
    context_object_name = 'csp_prog_list'

class Nop(generic.TemplateView):

    def check_post(self, request):

        template_name = 'nop.html'
        message = "Nop! Login First."

        return render(request, template_name, {"message":message})

def check_post(request):

    template_name = 'csp_prog_success.html'

    if request.method == "POST":
        form = Csp_prog_form(request.POST)
        if form.is_valid():
            prog = form.save(commit=False)
            prog.user_id = request.user.first_name
            prog.user_name = request.user.username
            prog.csp_prog_save()
            message = "Success!"
            return render(request, template_name, {"message":message})

    else:
        template_name = 'csp_prog_insert.html'
        form = Csp_prog_form
        return render(request, template_name, {"form" : form})

    # QnA~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # QnA~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Csp_prog_board_qna(generic.TemplateView):

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated == False:
            return render(self.request, 'nop.html', {"message": "Nop! Login First."})

        elif request.user.last_name != 'prog' and request.user.last_name != 'admin':
            return render(self.request, 'nop.html', {"message": "Nop! You are not programming member!"})

        template_name = 'prog_board_qna.html'
        csp_prog_qna = Csp_prog_list_qna.objects
        prog_page_list = Csp_prog_list_qna.objects.all().order_by('-no')
        paginator = Paginator(prog_page_list, 10)
        page = request.GET.get('page')
        posts = paginator.get_page(page)

        return render(request, template_name, {'csp_prog_qna': csp_prog_qna, 'posts': posts, 'top': prog_page_list})

class Csp_prog_detail_qna(generic.DetailView):

    model = Csp_prog_list_qna
    template_name = 'csp_prog_detail_qna.html'
    context_object_name = 'csp_prog_list_qna'

class Csp_prog_update_qna(generic.UpdateView):

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated == False:
            return render(self.request, 'nop.html', {"message": "Nop! Login First."})

        elif request.user.last_name != 'prog' and request.user.last_name != 'admin':
            return render(self.request, 'nop.html', {"message": "Nop! You are not programming member!"})

    model = Csp_prog_list_qna
    fields = ('title', 'content', 'is_complete')
    template_name = 'csp_prog_update_qna.html'
    success_url = '/progboard/qna'

    def form_valid(self, form):
        form.save()
        return render(self.request, 'csp_prog_success_qna.html', {"message": "Update Success!"})

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

class Csp_prog_delete_qna(generic.DeleteView):
    model = Csp_prog_list_qna
    success_url = '/progboard/qna'
    context_object_name = 'csp_prog_list_qna'

def check_post_qna(request):

    template_name = 'csp_prog_success_qna.html'

    if request.method == "POST":
        form = Csp_prog_form_qna(request.POST)
        if form.is_valid():
            prog = form.save(commit=False)
            prog.user_id = request.user.first_name
            prog.user_name = request.user.username
            prog.csp_prog_save_qna()
            message = "Success!"
            return render(request, template_name, {"message":message})

    else:
        template_name = 'csp_prog_insert_qna.html'
        form = Csp_prog_form_qna
        return render(request, template_name, {"form" : form})