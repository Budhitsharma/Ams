from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login as my_login, logout as my_logout
from django.contrib.auth.models import User
from django.utils import timezone

# Create your views here.
def login(request):
        if request.method == "POST":
              username = request.POST.get("user-name")
              password = request.POST.get("User-Password")
              user = authenticate(request, username = username, password = password)
              if user is not None:
                    my_login(request, user)
                    return redirect('dashboard')
              else:
                    messages.error(request, "User-Name or Password are incorrect!")
                    return redirect('login')
        return render(request, 'myapp/login.html')

def signup(request):
    if request.method == "POST":
          username = request.POST.get("user-name")
          email = request.POST.get("User-Email")
          contact = request.POST.get("contact-no")
          password = request.POST.get("User-Password")
          confirm_password = request.POST.get("Confirm-Password")         

          if password != confirm_password:
               messages.error(request, 'Passwords do not match.')
               return redirect('signup')

          if EmployeeDetailmodel.objects.filter(contact=contact).exists():
               messages.error(request, 'User with this contact Number is already exists!')
               return redirect('signup')

          if User.objects.filter(username=username).exists():
               messages.error(request, 'User with this User Name is already exists!')
               return redirect('signup')

          if  User.objects.filter(email=email).exists():
               messages.error(request, 'User with this Email is already exists!')
               return redirect('signup')
          
          user = User.objects.create_user(username=username, email=email, password=password)
          new_user = EmployeeDetailmodel.objects.create(user=user, contact=contact)
          new_user.save()

          messages.success(request, 'Account created successfully!')
          return redirect('login')  
    return render(request, 'myapp/sign-up.html')

@login_required
def dashboard(request):
    if request.method == 'POST':
        current_datetime = timezone.now()
        user_details = EmployeeDetailmodel.objects.get(user=request.user)
        existing_record = Timemodel.objects.filter(employee=user_details, date_field=current_datetime.date(), start_time=current_datetime.time()).exists()
        if 'break' in request.POST:
            if existing_record:
                print("Break")
                # existing_record.break_start = current_datetime.time()
                # existing_record.save()

        elif 'start_time' in request.POST:
            if existing_record:
                print("Yesss") 
                # existing_record.end_time = current_datetime.time()
                # existing_record.duration = existing_record.end_time - existing_record.start_time  
                # existing_record.save()
            else: 
                print("Noooo")
                # my_start_time =Timemodel(employee=user_details, date_field=current_datetime.date(), start_time=current_datetime.time())
                # my_start_time.save()



    user_details = EmployeeDetailmodel.objects.get(user=request.user)
    try:
        time_model = Timemodel.objects.filter(employee=user_details).order_by('-date_field')[:4]
        data = {
            'usd':user_details,
            'time_model': time_model,
        }
        return render(request, 'myapp/dashboard.html', data)
    except ObjectDoesNotExist:
        time_model = None
  

def logout(request):
    my_logout(request)
    return redirect('login')

def myAttendance(request):
    return render(request, 'myapp/myAttendance.html')

def editprofile(request):
    return render(request, 'myapp/editprofile.html')

def colleagues(request):
    return render(request, 'myapp/colleagues.html')

def employeeList(request):
    emp = User.objects.all()
    data = {
        'employee':emp
    }
    return render(request, 'myapp/employeeList.html', data)

def requestedLeave(request):
    return render(request, 'myapp/requestedLeave.html')

def statusofLeave(request):
    return render(request, 'myapp/statusofLeave.html')

def leaveDetails(request):
    return render(request, 'myapp/leaveDetails.html')

def leaveApplication(request):
    return render(request, 'myapp/leaveApplication.html')

def employeesLeave(request):
    return render(request, 'myapp/employeesLeave.html')

def employeeDetails(request, user_id):
    try:
        emp = EmployeeDetailmodel.objects.get(user_id=user_id)
        data = {
            'emp' : emp
        }
        return render(request, 'myapp/employeeDetails.html', data)
    except EmployeeDetailmodel.DoesNotExist:
        return render(request, 'myapp/employee_not_found.html')

def employeeAttendance(request):
    return render(request, 'myapp/employeeAttendance.html')

def editEmployeesProfile(request, user_id):
    try:
        emp = EmployeeDetailmodel.objects.get(user_id=user_id)
        data = {
            'emp' : emp
        }
        return render(request, 'myapp/editEmployeesProfile.html', data)
    except:
        print("error")

def addEmployee(request):
    if request.method == "POST":
          username = request.POST.get("user-name")
          email = request.POST.get("User-Email")
          contact = request.POST.get("contact-no")
          password = request.POST.get("User-Password")
          confirm_password = request.POST.get("Confirm-Password")         

          if password != confirm_password:
               messages.error(request, 'Passwords do not match.')
               return redirect('addEmployee')

          if EmployeeDetailmodel.objects.filter(contact=contact).exists():
               messages.error(request, 'User with this contact Number is already exists!')
               return redirect('addEmployee')

          if User.objects.filter(username=username).exists():
               messages.error(request, 'User with this User Name is already exists!')
               return redirect('addEmployee')

          if User.objects.filter(email=email).exists():
               messages.error(request, 'User with this Email is already exists!')
               return redirect('addEmployee')
          
          user = User.objects.create_user(username=username, email=email, password=password)
          new_user = EmployeeDetailmodel.objects.create(user=user, contact=contact)
          new_user.save()

          messages.success(request, 'Account created successfully!')
          return redirect('employeeList')  
    return render(request, 'myapp/addEmployee.html')
