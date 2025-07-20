from django.shortcuts import render, redirect
from .forms import CreateUserForm
from .models import Profile


# Create your views here.
def index(request):
    return render(request, 'app_aws/index.html')

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            current_user = form.save(commit=False)
            form.save()
            profile= Profile.objects.create(user=current_user)
            return redirect("my-login")
    else:
        form = CreateUserForm()
        context = {'form': form}
        return render(request, 'app_aws/register.html', context)

def my_login(request):
    return render(request, 'app_aws/my-login.html')

def dashboard(request):
    return render(request, 'app_aws/dashboard.html')

def profile_management(request):
    return render(request, 'app_aws/profile-management.html')

