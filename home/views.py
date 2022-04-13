from os import uname_result
from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
# Create your views here.
def index(request):
    context={
        "variable":"This is a food"
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,'about.html')

def course(request):
    return render(request,'course.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc= request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,'Your message has been sent successfully!!!')
    return render(request,'contact.html')

def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/main')
        
        else:
            return render(request,'login.html')
    return render(request,'login.html')    
def logoutuser(request):
    logout(request)
    return redirect('/login')
def main(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'main.html')
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('uname1')
        lname = request.POST.get('uname2')
        email = request.POST.get('email')
        pass1= request.POST.get('password')
        pass2= request.POST.get('cpassword')
        phone = request.POST.get('cnumber')
        
        #create a new user
        myuser = User.objects.create_user(username=username, email=email,password=pass1,first_name=fname,last_name=lname)
        
        myuser.save();
        messages.success(request,"Your account has been created successfully!!!")
        return redirect('/login')
        
    # else:
    #     return HttpResponse('404 - Not Found')
    return render(request,'signup.html')



def python(request):
    return render(request,'python.html')
def cpp(request):
    return render(request,'cpp.html')
    
def c(request):
    return render(request,'c.html')
def dart(request):
    return render(request,'dart.html')

def java(request):
    return render(request,'java.html')    
def js(request):
    return render(request,'js.html')