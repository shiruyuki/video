from ..lib.base_render import render_to_response
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect,reverse


class Login(View):

    LOGIN_TEMPLATE = '/dashboard/auth/login.html'
    ADMIN_TEMPLATE = '/dashboard/auth/admin.html'

    def get(self,request):

        data = {
            'username_error': '',
            'password_error': ''
        }

        if request.user.is_authenticated:
            return redirect(reverse('admin'))
        return render_to_response(request, self.LOGIN_TEMPLATE,data)

    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.filter(username=username,is_staff=True)

        print("user:",user)
        data = {
            'username_error': '',
            'password_error': ''
        }

        if not user:
            data["username_error"]="用户名不存在"
            return render_to_response(request, self.LOGIN_TEMPLATE,data)

        auth = authenticate(username=username, password=password)
        print(auth)
        if not auth:
            data["password_error"] = "密码错误"
            return render_to_response(request, self.LOGIN_TEMPLATE, data)

        login(request,auth)

        return redirect(reverse('admin'))


class Logout(View):

    def get(self,request):
        logout(request)
        return redirect(reverse('login'))


class AdminMessage(View):

    def get(self,request):

        users = User.objects.filter(is_staff=True)
        return render_to_response(request,'/dashboard/auth/admin.html',{"users":users})

