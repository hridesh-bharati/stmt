from django.urls import path
from .views import homePage, aboutUs, loginUser, logoutUser

urlpatterns = [
    path('', homePage, name="home"),
    path('about/', aboutUs, name="about"),
    path('login/', loginUser, name="login"),   # ✅ FIX
    path('logout/', logoutUser, name="logout"), # ✅ FIX
]