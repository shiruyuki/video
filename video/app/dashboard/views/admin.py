from video.app.lib.base_render import render_to_response
from django.views.generic import View
from django.contrib.auth.models import User
from app.utils.auth import dashboard_auth_login
from django.shortcuts import redirect,reverse,HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.models import User



class AdminMessage(View):

    @dashboard_auth_login
    def get(self,request):

        if not request.user.is_authenticated:
            return redirect(reverse('login'))

        users = User.objects.filter(is_staff=True).order_by()
        # paginator = Paginator(users, 3)
        # page = paginator.page(1)
        return render_to_response(request,'/dashboard/auth/admin.html',{"users":users})


class DeleteAdminMessage(View):

    @dashboard_auth_login
    def get(self,request,admin_id):
        User.objects.filter(id=admin_id).delete()
        return redirect(reverse('admin'))


class AddAdminMessage(View):

    @dashboard_auth_login
    def get(self,request):

        return render_to_response(request, '/dashboard/auth/add_admin.html',)

    def post(self,request):

        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_pwd = request.POST.get("confirm_pwd")
        is_active = request.POST.get("is_active")
        import json
        if not all([username,password,confirm_pwd]):
            return HttpResponse(json.dumps({"error":"用户名、密码或确认密码不能为空","code":400}))

        if password != confirm_pwd:
            return HttpResponse(json.dumps({"error": "两次密码不一致", "code": 400}))

        exists = User.objects.filter(username=username, is_staff=True).exists()
        if exists:
            return HttpResponse(json.dumps({"error": "用户名存在", "code": 400}))

        try:
            user = User.objects.create(
                username=username,
                password=password,
                is_staff = is_active,
                is_active = 1
            )
        except:
            return HttpResponse(json.dumps({"error": "添加用户异常", "code": 400}))

        return HttpResponse(json.dumps({"code":200}))


class UpdateAdminMessage(View):

    @dashboard_auth_login
    def get(self,request,admin_id):

        user = User.objects.filter(id=int(admin_id)).first()
        return render_to_response(request,"/dashboard/auth/update_admin.html",{"user":user})

    def post(self,request,admin_id):
        import json
        username = request.POST.get("username")
        is_superuser = request.POST.get("is_superuser")
        is_active = request.POST.get("is_active")

        if not username:
            return HttpResponse(json.dumps({"error":"用户名不能为空","code":400}))

        try:
            user = User.objects.filter(id=int(admin_id)).first()
            user.username=username
            user.is_superuser = is_superuser
            user.is_active = is_active
            user.save()
        except:
            return HttpResponse(json.dumps({"error":"修改失败","code":400}))

        return  HttpResponse(json.dumps({"code":200}))
