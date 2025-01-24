from lib2to3.fixes.fix_input import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'authentication/index.html')

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1==pass2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('signup')
            else:
                myuser = User.objects.create_user(username,email,pass1)
                myuser.save()

                # user_model = User.objects.get(username)
                # new_profile = Profile.objects.create(myuser=user_model, id_myuser=user_model.id)
                # new_profile.save()

        else:
            messages.info(request,'password do not match')
            return redirect('signup')
        
        # myuser.first_name = fname
        # myuser.last_name = lname
        
        messages.success(request, "Your account has been successfully created")
        return redirect('index')

    return render(request, "authentication/signup.html")

def signin(request):

   
    return render(request, "authentication/signin.html")
def index(request):

     if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            fname = user.username
            return render(request,"authentication/signin.html",{'fname': fname})
        else:
            messages.error(request,"Bad credentials")
            return redirect('signin')

     return render(request, "authentication/index.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('home')


def cart(request):


   
    return render(request, 'cart.html', context)