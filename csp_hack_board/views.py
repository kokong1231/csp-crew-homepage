from django.shortcuts import render, get_object_or_404, redirect
from .models import Csp_hack_list, Csp_hack_list_qna, Hack_comment, Hack_comment_qna
from .forms import Csp_hack_form, Csp_hack_form_qna, Hack_CommentForm, Hack_CommentForm_qna

# Create your views here.

from django.views import generic
from django.core.paginator import Paginator


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

def csp_hack_detail(request, pk):
    question = get_object_or_404(Csp_hack_list, pk=pk)

    if request.method == "POST":
        comment_form = Hack_CommentForm(request.POST)
        comment_form.instance.user_name = request.user.first_name
        comment_form.instance.no_id = pk
        comment_form.instance.user_id = request.user.username
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.csp_hack_save()

    comment_form = Hack_CommentForm()
    comments = question.comments.all()

    return render(request, 'csp_hack_detail.html',
                  {'csp_hack_list': question, "comments": comments, "comment_form": comment_form})

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

def csp_hack_detail_qna(request, pk):
    question = get_object_or_404(Csp_hack_list_qna, pk=pk)

    if request.method == "POST":
        comment_form = Hack_CommentForm_qna(request.POST)
        comment_form.instance.user_name = request.user.first_name
        comment_form.instance.no_id = pk
        comment_form.instance.user_id = request.user.username
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.csp_hack_save()

    comment_form = Hack_CommentForm_qna()
    comments = question.comments.all()

    return render(request, 'csp_hack_detail_qna.html',
                  {'csp_hack_list_qna': question, "comments": comments, "comment_form": comment_form})

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

def comment_update(request, comment_id):
    comment = get_object_or_404(Hack_comment, pk=comment_id)

    if request.user.is_authenticated == False:
        return render(request, 'nop.html', {"message": "Nop! Login First."})

    elif request.user.last_name != 'hack' and request.user.last_name != 'admin':
        return render(request, 'nop.html', {"message": "Nop! You are not hacking member!"})

    if request.method == "POST":
        form = Hack_CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('/hackboard/close/')
    else:
        form = Hack_CommentForm(instance=comment)
    return render(request,'hack_comment_update.html', {'form':form, 'hack_comment':comment})

def comment_delete(request, pk, comment_id):
    comment = get_object_or_404(Hack_comment, pk=comment_id)

    if request.user.is_authenticated == False:
        return render(request, 'nop.html', {"message": "Nop! Login First."})

    elif request.user.last_name != 'hack' and request.user.last_name != 'admin':
        return render(request, 'nop.html', {"message": "Nop! You are not hacking member!"})

    if request.method == "POST":
        comment.delete()
        return redirect('/hackboard/' + str(pk) + '/detail/')
    else:
        return render(request, 'hack_comment_delete.html', {'object':comment})

def closed_page(request):
    template_name = 'closed_page.html'
    return render(request, template_name)

def comment_update_qna(request, comment_id):
    comment = get_object_or_404(Hack_comment_qna, pk=comment_id)

    if request.user.is_authenticated == False:
        return render(request, 'nop.html', {"message": "Nop! Login First."})

    elif request.user.last_name != 'hack' and request.user.last_name != 'admin':
        return render(request, 'nop.html', {"message": "Nop! You are not hacking member!"})

    if request.method == "POST":
        form = Hack_CommentForm_qna(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('/hackboard/close/')
    else:
        form = Hack_CommentForm(instance=comment)
    return render(request,'hack_comment_update.html', {'form':form, 'hack_comment':comment})

def comment_delete_qna(request, pk, comment_id):
    comment = get_object_or_404(Hack_comment_qna, pk=comment_id)

    if request.user.is_authenticated == False:
        return render(request, 'nop.html', {"message": "Nop! Login First."})

    elif request.user.last_name != 'hack' and request.user.last_name != 'admin':
        return render(request, 'nop.html', {"message": "Nop! You are not hacking member!"})

    if request.method == "POST":
        comment.delete()
        return redirect('/hackboard/qna/' + str(pk) + '/detail/')
    else:
        return render(request, 'hack_comment_delete.html', {'object':comment})
