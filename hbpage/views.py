# hbpage\views.py
from .models import Admission
from .models import StudentRegistration
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Admission, ContactInquiry
from django.db.models import Count

# --- Static Pages ---
def homePage(request):
    return render(request, "index.html")

def aboutUs(request):
    return render(request, "about.html")

def contactUs(request):
    if request.method == "POST":
        ContactInquiry.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )

        messages.success(request, "Message send Successfully !")
        return redirect('contact')

    return render(request, "contact.html")

def galleryPage(request):
    return render(request, "gallery.html")

 
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

def contact_view(request):
    if request.method == "POST":
        ContactInquiry.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        messages.success(request, "Aapka sandesh humein mil gaya hai!")
        return redirect('contact')
    return render(request, 'contact.html')

def delete_inquiry(request, id):
    inquiry = get_object_or_404(ContactInquiry, id=id)

    inquiry.delete()

    messages.success(request, "Inquiry deleted successfully.")

    return redirect('dashboard')

def register_student(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')

        if name and email and city:

            StudentRegistration.objects.create(
                name=name,
                email=email,
                city=city
            )

            messages.success(request, "Registration successful!")

        else:
            messages.error(request, "Please fill all fields.")

    return redirect('home')

def admission_view(request):
    if request.method == "POST":
        new_admission = Admission(
            student_photo=request.FILES.get('student_photo'),
            student_name=request.POST.get('student_name'),
            father_name=request.POST.get('father_name'),
            mother_name=request.POST.get('mother_name'),
            phone=request.POST.get('phone'),
            adhar_no=request.POST.get('adhar_no'),
            address=request.POST.get('address'),
            admission_class=request.POST.get('admission_class'),
            gender=request.POST.get('gender'),
            dob=request.POST.get('dob'),
        )
        new_admission.save()
        messages.success(request, "Application submitted successfully!")
        return redirect('home')
    return render(request, 'admission.html')

@login_required(login_url='login')
def dashboardPage(request):

    admissions = Admission.objects.all().order_by("-id")

    total_count = admissions.count()
    registrations = StudentRegistration.objects.all().order_by('-id')
    nursery_count = admissions.filter(admission_class="Nursery").count()
    inquiries = ContactInquiry.objects.all().order_by('-id')
    # ---------- Chart Data ----------
    class_data = (
        Admission.objects
        .values('admission_class')
        .annotate(total=Count('id'))
        .order_by('admission_class')
    )

    class_labels = [item['admission_class'] for item in class_data]
    class_totals = [item['total'] for item in class_data]

    recent_students = (
        Admission.objects
        .order_by('-submitted_at')[:7]
    )

    student_names = [student.student_name for student in recent_students]
    student_ids = [student.id for student in recent_students]

    context = {
        "admissions": admissions,
        'registrations': registrations,
        "total_count": total_count,
        "nursery_count": nursery_count,
        "inquiries": inquiries,

        # Charts
        "class_labels": class_labels,
        "class_totals": class_totals,
        "student_names": student_names,
        "student_ids": student_ids,
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