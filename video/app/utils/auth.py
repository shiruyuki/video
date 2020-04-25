import functools
from django.shortcuts import redirect,reverse


def dashboard_auth_login(func):
    @functools.wraps(func)
    def wraps(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('login'))
        return func(self,request,*args,**kwargs)
    return wraps