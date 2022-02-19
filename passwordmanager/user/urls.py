from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login_request,name="loginrequest"),
    path('register',views.register_request,name="registerrequest"),
    path('logout',views.logout_request,name="logoutrequest"),
]
