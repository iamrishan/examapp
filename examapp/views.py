from django.shortcuts import render
from . models import *

# Create your views here.


def fn_index(request):
    return render(request, 'index.html')


def fn_login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        user_pass = request.POST['password']

        login_obj = Login.objects.get(username=user_name)

        if user_name == login_obj.username and user_pass == login_obj.password:
            request.session['id'] = login_obj.id
            return render(request, 'adminhome.html')
    return render(request, 'index.html')


def fn_reg_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']

        login_obj = Login(username=username, password=password)
        login_obj.save()

        if login_obj.id > 0:
            register_obj = Reg_Student(
                name=name, username=username, password=password, login_user=login_obj)
            register_obj.save()
            if register_obj.id > 0:
                return render(request, 'adminhome.html', {"message": "You have successfully registered a student"})
    return render(request, 'adminhome.html')
