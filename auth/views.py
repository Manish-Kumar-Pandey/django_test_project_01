from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text


# Create your views here.
def home(request):
    return render(request,"auth/index.html")

@csrf_exempt
def signup(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        psw = request.POST.get('psw')
        psw2 = request.POST.get('psw2')
        address = request.POST.get('address')


        myuser = User.objects.create_user(username, email, psw)


        myuser.save()
        messages.success(request, "Your acount has been successfully created.")
        return render(request,"auth/index.html")

    return render(request,"auth/signup.html")



@csrf_exempt
def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        psw = request.POST.get('psw')


        user = authenticate(username=username, password = psw)

        if user is not None:
            login(request, user)
            return render(request, "auth/Home-page.html")

        else:
            messages.error("Wrong Credentials")
            return redirect('home')

    return render(request,"auth/signin.html")

def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')
