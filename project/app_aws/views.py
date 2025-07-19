from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app_aws/index.html')

def register(request):
    return render(request, 'app_aws/register.html')

def my_login(request):
    return render(request, 'app_aws/my-login.html')

def dashboard(request):
    return render(request, 'app_aws/dashboard.html')

def profile_management(request):
    return render(request, 'app_aws/profile-management.html')

