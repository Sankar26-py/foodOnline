from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import UserForm
from .models import User
from django.contrib import messages

# Create your views here.

def registerUser(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            #create user using form data
            # password=form.cleaned_data['password']
            # user=form.save(commit=False)
            # user.role=User.CUSTOMER 
            # user.set_password(password)
            # user.save()

            #create user using createdUser method
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request,"Your Account has been Registered Successfully!")
            return redirect('registerUser')
        else:
            print("Invalid Form")
            print(form.errors)
            #raise form.ValidationError(form.errors)
    else:
        form = UserForm()
    return render(request,'accounts/registerUser.html',{'form':form})
