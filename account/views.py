from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import CustomUserChangeForm
from django.views import generic

# Password module
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

class Nop(generic.TemplateView):

    def check_post(self, request):

        template_name = 'nop.html'
        message = "Nop! Login First."

        return render(request, template_name, {"message":message})

def sign(request):

    if request.user.is_authenticated:
        return redirect('/main/')

    if request.method == "POST":

        for x in request.POST["username"]:
            if x.isalnum() == False:
                return render(request, 'sign_fail.html', {"message": '사용할 수 없는 ID 입니다.'})

        if request.POST["password1"] == request.POST["password2"] and len(request.POST["password1"]) <= 7:
            return render(request, 'sign_fail.html', {"message": '패스워드는 8자리 이상 입력하십시오.'})

        elif request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password1"],
                first_name=request.POST["first_name"], last_name=request.POST["last_name"])
            auth.login(request, user)
            return redirect('/main/')
        return render(request, 'sign_fail.html', {"message":'패스워드가 일치하지 않습니다.'})

    return render(request, 'sign.html')

def login(request):

    if request.user.is_authenticated:
        return redirect('/main/')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/main/')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/main/')

def update(request):

    if request.user.is_authenticated == False:
        return render(request, 'nop.html', {"message": "Nop! Login First."})

    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)

        for x in request.POST["username"]:
            if x.isalnum() == False:
                return render(request, 'sign_fail.html', {"message": '사용할 수 없는 ID 입니다.'})

        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('../user')

    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
        return render(request, 'user_update.html', {
            'user_update': user_change_form
    })

def user(request):
    if request.user.is_authenticated == False:
        return render(request, 'nop.html', {"message": "Nop! Login First."})

    return render(request, 'user.html')


def delete(request):

    if request.user.is_authenticated == False:
        return render(request, 'nop.html', {"message": "Nop! Login First."})

    if request.method == 'POST':
        request.user.delete()
        return redirect('/main/')

    return render(request, 'user_delete.html')

def change_password(request):

    if request.user.is_authenticated == False:
        return render(request, 'nop.html', {"message": "Nop! Login First."})

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if request.POST["new_password1"] == request.POST["new_password2"] and len(request.POST["new_password1"]) <= 7:
            return render(request, 'sign_fail.html', {"message": '패스워드는 8자리 이상 입력하십시오.'})

        elif form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return render(request, 'success.html', {"message": "성공적으로 변경되었습니다!"})
        else:
            return render(request, 'fail.html', {"message": "실패했습니다. 비밀번호를 정확히 입력해주세요."})
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })