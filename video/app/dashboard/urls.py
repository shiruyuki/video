from django.urls import path
from .views import AdminMessage,Login,Logout

urlpatterns = [
    path('admin/',AdminMessage.as_view() ,name ="admin"),
    path('login/',Login.as_view() ,name ="login"),
    path('logout/',Logout.as_view() ,name ="logout")
]