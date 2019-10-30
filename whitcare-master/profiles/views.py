from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProfileForm
from .models import Profile
from .forms import AccountForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')

def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            new_profile = form.save()
            return redirect(new_profile)
    else:
        form = ProfileForm()
    return render(request, 'userprofile_edit.html', { 'form': form })

def view_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'userprofile.html', { 'profile': profile })

def edit_profile(request, pk):
    user_profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            edited_profile = form.save()
            return redirect(edited_profile)
    else:
        form = ProfileForm(instance=user_profile)
    return render(request, 'userprofile_edit.html', { 'form': form })

def search_results(request):
    first_name = request.GET.get('first_name', '')
    last_name = request.GET.get('last_name', '')
    if not first_name and not last_name:
        results = None 
    else:
        results = Profile.objects.filter(
            first_name__startswith=first_name,
            last_name__startswith=last_name,
        )
    return render(request, 'searchresults.html', {'results': results})
  
def login(request):
    #If logging in
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            print("Email: ", email, ", Password: ", password)
            #Validate credentials
            user = authenticate(username=email, password=password)
            if user is not None:    #Credentials authenticated
                return render(request, 'index.html')
            else:   #Credentials invalid
                #Todo: add error message saying invalid credentials
                return render(request, 'login.html', { 'form' : form })
        else:
            return render(request, 'login.html')
    #Load blank page
    else:
        form = AccountForm()
    return render(request, 'login.html', { 'form' : form })

def create_account(request):
    #If creating account
    if request.method == 'POST':
        new_acc_form = AccountForm(request.POST)
        if new_acc_form.is_valid():
            email = new_acc_form.cleaned_data.get("email")
            password = new_acc_form.cleaned_data.get("password")

            #Check if user exists
            user, created = User.objects.get_or_create(username=email, email=email)
            if created: #new account created
                user.set_password(password)
                user.save()
                return redirect('login')

            #Todo: Add error message saying account already exists
    blank_form = AccountForm()
    return render(request, 'create_account.html', { 'form' : blank_form })
