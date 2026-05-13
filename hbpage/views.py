# hbpage\views.py
from .models import Admission
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# --- Static Pages ---
def homePage(request):
    return render(request, "index.html")

def aboutUs(request):
    return render(request, "about.html")

def contactUs(request):
    return render(request, "contact.html")

def galleryPage(request):
    return render(request, "gallery.html")

# --- Admission Logic (Merged into one function) ---
def admission_view(request):
    if request.method == "POST":
        new_admission = Admission(
            student_photo = request.FILES.get('student_photo'),
            student_name = request.POST.get('student_name'),
            father_name = request.POST.get('father_name'),
            mother_name = request.POST.get('mother_name'),
            phone = request.POST.get('phone'),
            adhar_no = request.POST.get('adhar_no'),
            address = request.POST.get('address'),
            admission_class = request.POST.get('admission_class'),
            # admission_date ki jagah auto_now_add use hota hai, par agar manually chahiye toh:
            # admission_date = request.POST.get('admission_date'), 
            gender = request.POST.get('gender'),
            dob = request.POST.get('dob'),
        )
        new_admission.save()
        messages.success(request, "Application submitted successfully!")
        return redirect('home')

    return render(request, 'admission.html')

# --- Admin Section ---

def loginUser(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("user_id"),
            password=request.POST.get("password")
        )

        if user:
            login(request, user)
            return redirect("dashboard") # Login ke baad seedha dashboard
        return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")

@login_required(login_url='login')
def dashboardPage(request):
    students = Admission.objects.all().order_by('-submitted_at')
    context = {
        'admissions': students,
        'total_count': students.count(),
        'nursery_count': students.filter(admission_class='Nursery').count(), # Extra stats
    }
    return render(request, "dashboard/index.html", context)


@login_required(login_url='login')
def delete_admission(request, pk):
    if request.method == "POST":
        student = get_object_or_404(Admission, pk=pk)
        student.delete()
        messages.error(request, "Admission record deleted!")
        return redirect('dashboard')
    return redirect('dashboard')

def logoutUser(request):
    logout(request)
    return redirect("login")