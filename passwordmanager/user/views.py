from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.



def login_request(request):
    if request.method == "GET":
        return render(request,"user/login.html")

    elif request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return render(request,"managerapp/index.html")
        else:
            return render(request,"user/login.html",{"error" : "Yanlış kullanıcı adı veya parola girdiniz ! "})

    else:
        return redirect("registerrequest")





def register_request(request):
    if request.method == "GET":
        return render(request,"user/register.html")

    elif  request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
     
     
        if User.objects.filter(username = username).exists():
            return render(request,"user/register.html",{"error" : "Bu kullanıcı adı veya email önceden alınmış !"})
        

        user = User.objects.create_user(username = username,password = password,email = email)
        user.save()
        return render(request,"managerapp/index.html")


    else:
        return redirect("registerrequest")


@login_required(login_url='/user/login')
def logout_request(request):
    logout(request)
    return redirect("loginrequest")