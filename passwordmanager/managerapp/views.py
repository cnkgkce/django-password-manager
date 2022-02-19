from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from user import models as user_model
from cryptography.fernet import Fernet
import random,string
# Create your views here.



@login_required(login_url='/user/login')
def home(request):
    if request.method == "GET":
            
        user_passwords = user_model.Password.objects.filter(username = request.user.username)
        decrypted_passwords = []
        keys = []
        ids = []

        for encrypted_password in user_passwords:
            keys.append(encrypted_password.key)
            ids.append(encrypted_password.id)
            fernet = Fernet(encrypted_password.fkey)
            decrypted_password = fernet.decrypt(encrypted_password.password).decode()
            decrypted_passwords.append(decrypted_password)

        mylist = zip(decrypted_passwords,keys,ids)
        
        return render(request,"managerapp/index.html",{
        'mylist' : mylist,
            })
        
@login_required(login_url='/user/login')
def about(request):
    return render(request,"managerapp/about.html")    



@login_required(login_url='/user/login')
def add_password(request):
    if request.method == "GET":
        return render(request,"managerapp/addpassword.html")
    
    elif request.method =="POST":
            
        key = request.POST['key']
        password = request.POST['password']
        fkey = Fernet.generate_key()
        fernet = Fernet(fkey)

        securePass = fernet.encrypt(password.encode())

        #password_model = user_model.Password(key = key, password = securePass,username=request.user.username, fkey = fkey)
        #password_model.save()
        user_model.Password.objects.update_or_create(key = key, password = securePass, username = request.user.username ,fkey = fkey )
        return redirect("home")
        
    else:
        return redirect("home")



@login_required
def edit_record(request,id):
    if request.method =="GET":
        record = user_model.Password.objects.get(id = id)
        return render(request,"managerapp/edit.html",{"record" : record})

    add_password(request)
    delete_record(request,id)
    return redirect("home")



@login_required
def delete_record(request,id):
    record = user_model.Password.objects.get(id = id)
    record.delete()
    return redirect("home")


@login_required
def generate_password(request):
    if request.method == "GET":
        return render(request,"managerapp/generate_password.html")

    #request is post

    input_from_user = int(request.POST['passcharnum'])
    #possible_characters = "abcdefghijklmnopqrstuvwxyz1234567890"
    possible_characters = string.printable

    random_character_list = [random.choice(possible_characters) for i in range(input_from_user)]
    random_password = "".join(random_character_list)
    return render(request,"managerapp/generate_password.html",{"password" : random_password})