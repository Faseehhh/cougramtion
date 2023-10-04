from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegistrationForm


def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        # Authenticate the user based on email and password
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # User is authenticated, log them in
            login(request, user)
            return redirect("index")  # Redirect to the desired page after successful login
        else:
            # Authentication failed, show an error message or handle it as needed
            error_message = "Invalid email or password. Please try again."
            return render(request, "login.html", {"error_message": error_message})

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

def index(request):
    return render(request, "index.html")


def Recommend(request):
    return render(request, "recommend.html")







