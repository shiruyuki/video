from django.urls import path
from .views.auth import Login,Logout
from .views.admin import AdminMessage,DeleteAdminMessage,AddAdminMessage,UpdateAdminMessage

urlpatterns = [
    path('admin/',AdminMessage.as_view() ,name ="admin"),
    path('add_admin/',AddAdminMessage.as_view() ,name ="add_admin"),
    path('update_admin/<str:admin_id>/',UpdateAdminMessage.as_view() ,name ="update_admin"),
    path('delete_admin/<str:admin_id>',DeleteAdminMessage.as_view() ,name ="delete_admin"),
    path('login/',Login.as_view() ,name ="login"),
    path('logout/',Logout.as_view() ,name ="logout")
]