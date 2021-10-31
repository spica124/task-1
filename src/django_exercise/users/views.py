from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from .models import User
# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = (request.POST["username"])
        password = (request.POST["password"])
        user = authenticate(username=username,password=password)
        if user is not None:
            print("인증성공")
            login(request,user)
        else :
            print("인증실패")
    return render(request,"users/login.html")

def logout_view(request):
    logout(request)
    return redirect("user:login")

def signup_view(request):
    if request.method == "POST":
        print(request.POST)
        username  = request.POST["username"]
        password  = request.POST["password"]
        email  = request.POST["email"]
        favorite  = request.POST["favorite"]
        student_id = request.POST["student_id"]
        gender  = request.POST["gender"]
        
        Department  = request.POST["Department"]

        user = User.objects.create_user(username, email, password)
        user.favorite = favorite
        user.student_id = student_id
        user.gender = gender
        
        user.Department = Department
        user.save()
        return redirect("user:login")
    return render(request, "users/signup.html")