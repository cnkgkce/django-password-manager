from django.urls import path
from . import views


urlpatterns = [
    path("",views.home,name="home"),
    path("about",views.about,name="about"),
    path("addpassword",views.add_password,name="addpassword"),
    path("delete-record/<int:id>",views.delete_record,name="delete-record"),
    path("edit-record/<int:id>",views.edit_record,name="edit-record"),
    path("generate-password",views.generate_password,name="generate-password"),
]
