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
        paginator = Paginator(users, 3)
        page = paginator.page(1)
        return render_to_response(request,'/dashboard/auth/admin.html',{"users":page.object_list,"error":""})


class DeleteAdminMessage(View):

    @dashboard_auth_login
    def get(self,request,admin_id):
        User.objects.filter(id=admin_id).delete()
        return redirect(reverse('admin'))


class AddAdminMessage(View):

    def post(self,request):

        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_pwd = request.POST.get("confirm_pwd")
        import json
        if not all([username,password,confirm_pwd]):
            return HttpResponse(json.dumps({"error":"用户名、密码或确认密码不能为空","code":400}))
            # return render_to_response(request,self.TEMPLATE,{"error":"用户名、密码或确认密码不能为空"})

        if password != confirm_pwd:
            return HttpResponse(json.dumps({"error": "两次密码不一致", "code": 400}))

        exists = User.objects.filter(username=username, is_staff=True).exists()
        if exists:
            return HttpResponse(json.dumps({"error": "用户名存在", "code": 400}))

        try:
            user = User.objects.create(
                username=username,
                password=password,
                is_staff = True,
                is_active = True
            )
        except:
            return HttpResponse(json.dumps({"error": "添加用户异常", "code": 400}))

        return HttpResponse(json.dumps({"code":200}))


class UpdateAdminMessage(View):

    @dashboard_auth_login
    def get(self,request,admin_id):

        user = User.objects.filter(id=admin_id).first()
        import json
        return HttpResponse(json.dumps({"username":user.username,"is_active":user.is_active,"is_staff":user.is_staff}))

    def post(self,request):
        pass