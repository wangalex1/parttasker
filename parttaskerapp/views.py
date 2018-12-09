from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from parttaskerapp.forms import UserForm, CompanyForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return redirect(company_home)

@login_required(login_url='/company/sign-in/')
def company_home(request):
    return render(request, 'company/home.html', {})

def company_sign_up(request):
    user_form = UserForm()
    restaurant_form = CompanyForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        restaurant_form = CompanyForm(request.POST, request.FILES)

        if user_form.is_valid() and company_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_company = restaurant_form.save(commit=False)
            new_company.user = new_user
            new_company.save()

            login(request, authenticate(
                username = user_form.cleaned_data["username"],
                password = user_form.cleaned_data["password"]
            ))

            return redirect(company_home)

    return render(request, "company/sign_up.html", {
        "user_form": user_form,
        "company_form": company_form
    })
