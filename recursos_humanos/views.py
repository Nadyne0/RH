from django.shortcuts import render
from django.contrib.auth import authenticate, login

# from django.contrib import messages
from django.shortcuts import redirect
from recursos_humanos.forms import RegisterForm


def home_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("")

    return render(request, "home.html")


def register_view(request):
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            request.session["message"] = "Registro bem-sucedido!"
            return redirect("/")

    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})
