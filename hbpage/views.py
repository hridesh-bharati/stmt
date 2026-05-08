from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def homePage(request):
    return render(request, "index.html")

def aboutUs(request):
    return render(request, "about.html")

def loginUser(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("user_id"),
            password=request.POST.get("password")
        )

        if user:
            login(request, user)
            return redirect("/")
        return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect("/login/")