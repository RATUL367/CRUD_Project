from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.


# This Function Will Add New Item and Show All Items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pwd = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pwd)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})

# This Function Will Update/Edit The Data
def update_data(request, id):
    if request.method == 'POST':
        update_obj = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=update_obj)
        if fm.is_valid():
            fm.save()
    else:
        update_obj = User.objects.get(pk=id)
        fm = StudentRegistration(instance=update_obj)
    return render(request, 'enroll/updatestudent.html', {'form':fm})




# This Function Will Use For Delete Data
def delete_data(request, id):
    if request.method == 'POST':
        del_obj = User.objects.get(pk=id)
        del_obj.delete()
        return HttpResponseRedirect('/')
