from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import EmployeeForm, LoginForm, SignUpForm
from .models import Employee,Login
from django.db.models import Q
# Create your views here.
def loginfn(request):
    if request.method == "POST":  
        form = LoginForm()
        user=request.POST.get("Username")
        pwd=request.POST.get("Password")
        p=Login.objects.filter(Q(Username=user) & Q(Password=pwd))
        if p:
            return redirect('/show')  
        else:
            msg="Invalid Username or Password ! Try again ! "
            return render(request,'login.html',{'form':form,'msg':msg})
    else:
        form = LoginForm()
        return render(request,'login.html',{'form':form})
def register(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass
    else:
        form=SignUpForm(request.POST)  
    return render(request,'register.html',{'form':form})

def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'emp.html',{'form':form})  
def show(request):
    employees = Employee.objects.all()
    return render(request,"show.html",{'employees':employees})
def edit(request,id):
    employee = Employee.objects.get(Code=id)
    return render(request,"edit.html",{'employee':employee})
def update(request,id):
    employee = Employee.objects.get(Code=id)
    form = EmployeeForm(request.POST,instance=employee)
    if form.is_valid():  
        form.save()
        return redirect("/show")
    return render(request,"edit.html",{'employee':employee})
def delete(request,id):
    employee = Employee.objects.get(Code=id)
    employee.delete()
    return redirect("/show")
def search(request):
    return render(request,'search.html')
def search_by_code(request):
    if request.method=='POST':
        id=request.POST.get('Code')
        employees = Employee.objects.get(Code=id)
        return render(request,"show.html",{'employees':employees})
    else:
        return render(request,'searchbycode.html')