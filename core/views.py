from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import uimage
# Create your views here.
@login_required(login_url="/login")
def index(request):
    return  render(request,'index.html')

# handle Signup 
def handleSignup(request):
    # Check the request is Post or not 
    if request.method == 'POST':
        # Take the all parameters 
        username = request.POST['username']
        firstName = request.POST['fname']
        lastName = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']

        # Check whether the parameters is valid or not 
        if len(username) > 15:
            messages.error(request, "Username must be under 15 characters ")
            return redirect('/signup')

        if not username.isalnum():
            messages.error(request, "Username must only contain letter and characters  ")
            return redirect('/signup')

        if len(pass1) < 8:
            messages.error(request, "Password is too small ")
            return redirect('/signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = firstName
        myuser.last_name = lastName
        myuser.save()
        messages.success(request, "Your iUploader   account has been successfull created ")
        return redirect('/')
    else:
        return render(request, "signup.html")


#  Login System 
def handleLogin(request):
    # Check the request is Post or not 
    if request.method == 'POST':
        # Take the all parameters 
        username = request.POST['loginusername']
        password = request.POST['loginpass']

        # Trying to authenticate
        user = authenticate(username=username, password=password)

        # Check whether the user exsists or not 
        if user is not None:
            login(request, user)
            messages.success(request, "succesfully Logged In ")
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password  ")
            return redirect('/')
    else:
        return render(request, 'login.html')


# Logout System 
def handleLogout(request):
    logout(request)
    return redirect('/')


def handleFile(request): 
       # Check the request is Post or not 
    if request.method == 'POST':
        user = User.objects.filter(username=request.user.username).first()
        image = request.FILES.get('image')
        u = uimage(user=user,image=image)
        u.save()
        messages.success(request, "Image Uploaded Successfully ")

        return render(request, 'index.html')