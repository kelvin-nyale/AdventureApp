
from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
from django.contrib import messages
from myApp.models import Users, Packages, Activities, Services
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import make_password
from decimal import Decimal, InvalidOperation
# from django.contrib.auth import get_user_model


# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        role = request.POST.get('role')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        
        # Check if user with this email already exists
        if Users.objects.filter(email=email).exists():
            messages.error(request, "User with this email already exists")
            return redirect('register')
        
        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')
        
        # Create new user
        user = Users.objects.create(
            username=username,
            email=email,
            role=role,
            password=make_password(password)
        )
        user.save()

        messages.success(request, "Registration successful! You can now log in.")
        return redirect('login')
        
        
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        print("username", username)
        # print("password", password)

        # Check if the username exists
        try:
            user_obj = Users.objects.get(username=username)
        except Users.DoesNotExist:
            messages.error(request, "Username does not exist.")
            return render(request, 'login.html')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        # print("user", user)
        if user is not None:
            auth_login(request, user)  # Log in the user
            
            # Check user role and redirect accordingly
            role = user_obj.role.lower()  
            if 'admin' in role:  
                return redirect('admin_dashboard')  
            elif 'instructor' in role:  
                return redirect('instructor_dashboard')
            elif 'user' in role:  
                return redirect('user_dashboard')  
            else:
                print("Logged in successfully")
                
        else:
            messages.error(request, "Invalid password.")
            return render(request, 'login.html')

    # messages.error(request, "Invalid password from function.")
    return render(request, 'login.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        role = request.POST.get('role')
        password = request.POST.get('password')

        # Check if a user with the given username already exists
        if Users.objects.filter(username=username).exists():
            messages.error(request, "User with this username already exists.")
            return redirect('add_user')

        # Create the user with a hashed password
        user = Users.objects.create(
            username=username, 
            email=email, 
            role=role, 
            password=make_password(password)  # Securely hash the password
        )

        messages.success(request, "User added successfully!")
        return redirect('users')  # Redirect to the user list page

    return render(request, 'add_user.html')

def users(request):
    users=Users.objects.all()
    return render(request, 'users.html', {'users':users})

def update_user(request, pk):  # Ensure it matches the URL
    user = get_object_or_404(Users, id=pk)

    if request.method == 'POST':
        user.username = request.POST.get('username', user.username)
        user.email = request.POST.get('email', user.email)
        user.role = request.POST.get('role', user.role)
        user.save()
        messages.success(request, "User updated successfully!")
        return redirect('users')  # Redirect to the user list

    return render(request, 'update_user.html', {'user': user})

def delete_user(request,pk):
    user=get_object_or_404(Users, id=pk)
    # user=Users.objects.get(Users,pk=id)
    if request.method == 'POST':
        user.delete()
        return redirect('users')
    return render(request, 'delete_user.html', {'user':user})

def instructor_dashboard(request):
    return render(request, 'instructor_dashboard.html')

def user_dashboard(request):
    return render(request, 'user_dashboard.html')

#PACKAGES FUNCTIONS
# def add_package(request):
#     if request.method == 'POST':
#         package_id = request.POST.get('package_id')
#         package_name = request.POST.get('package_name')
#         description = request.POST.get('description')
#         price = request.POST.get('price')

#         if Packages.objects.filter(package_name=package_name).exists():
#             messages.error(request, "This package already exists.")
#             return redirect('add_package')
        
#         package = Packages.objects.create(
#             package_id=package_id,
#             package_name=package_name,
#             description=description,
#             price=price
#         )
#         messages.success(request, "Package added successfully")
#         return redirect('packages')

#     return render(request, 'add_package.html')

def add_package(request):
    if request.method == 'POST':
        package_id = request.POST.get('package_id')
        package_name = request.POST.get('package_name')
        description = request.POST.get('description')
        price_str = request.POST.get('price')  # Get price as a string

        # Convert price to Decimal safely
        try:
            price = Decimal(price_str)
        except (InvalidOperation, TypeError, ValueError):
            messages.error(request, "Invalid price format. Please enter a valid number.")
            return redirect('add_package')

        if Packages.objects.filter(package_name=package_name).exists():
            messages.error(request, "This package already exists.")
            return redirect('add_package')

        package = Packages.objects.create(
            package_id=package_id,
            package_name=package_name,
            description=description,
            price=price
        )
        messages.success(request, "Package added successfully")
        return redirect('packages')

    return render(request, 'add_package.html')

def packages(request):
    packages=Packages.objects.all()
    return render(request, 'packages.html', {'packages':packages})   

def update_package(request, package_id):
    package = get_object_or_404(Packages, package_id=package_id) 


    if request.method == 'POST':
        package.package_id = request.POST.get('package_id', package.package_id)
        package.package_name = request.POST.get('package_name', package.package_name)
        package.description = request.POST.get('description', package.description)
        package.price = request.POST.get('price', package.price)
        package.save()

        messages.success(request, "Package Updated succesfully!")
        return redirect('packages')

    return render(request, 'update_package.html', { 'package':package })

def delete_package(request, package_id):
    package = get_object_or_404(Packages, package_id=package_id)
    if request.method == 'POST':
        package.delete()
        return redirect('packages')
    return render(request, 'delete_package.html', {'package':package})

def add_activity(request):
    if request.method == 'POST':
        activity_id = request.POST.get('activity_id')
        name = request.POST.get('name')

        if Activities.objects.filter(activity_id=activity_id).exists():
            messages.error(request, "This activity already exists!")
            return redirect('add_activity')
        
        activity = Activities.objects.create(
            activity_id = activity_id,
            name = name
        )
        messages.success(request, "Activity added successfully!")
        return redirect('activities')

    return render(request, 'add_activity.html')

def activities(request):
    activities = Activities.objects.all()
    return render(request, 'activities.html', {'activities': activities})

# def update_activity(request, id):
#     activity = get_object_or_404(Activities, id=id)

#     if request.method == 'POST':
#         activity.activity_id = request.POST.get(activity_id, 'activity_id')
#         activity.name = request.POST.get(name, 'name')
#         activity.save()

#         messages.success(request, "Activity updated successfully")
#         return redirect('activitiea')

#     return render(request, 'update_activity.html', {'activity': activity})
def update_activity(request, id):
    activity = get_object_or_404(Activities, id=id)

    if request.method == 'POST':
        activity.activity_id = request.POST.get('activity_id', activity.activity_id)
        activity.name = request.POST.get('name', activity.name)
        activity.save()

        messages.success(request, "Activity updated successfully!")
        return redirect('activities')

    return render(request, 'update_activity.html', {'activity': activity})

def delete_activity(request, id):
    activity = get_object_or_404(Activities, id=id)
    
    if request.method == 'POST':
        activity.delete()
        messages.success(request, 'Activity deleted successfully')
        return redirect('activities')
    return render(request, 'delete_activity.html', {'activity': activity})

def add_service(request):
    if request.method == 'POST':
        service_id = request.POST.get('service_id')
        service_name = request.POST.get('service_name')

        if Services.objects.filter(service_name=service_name).exists():
            messages.error(request, "Service Already Exists!")
            return redirect('services')
        
        service = Services.objects.create(
            service_id=service_id,
            service_name=service_name
        )
        messages.success(request, f"{service.service_name} added successfully!")
        return redirect('services')

    return render(request, 'add_service.html')

def services(request):
    services = Services.objects.all()
    return render(request, 'services.html', {'services': services})

def update_service(request, id):
    service = get_object_or_404(Services, id=id)

    if request.method == 'POST':
        service_id = request.POST.get('service_id', service.service_id)
        service_name = request.POST.get('service_name', service.service_name)
        service.save()

        messages.success(request, "Service updated")
        return redirect('services')
    return render(request, 'update_service.html', {'service': service})

def delete_service(request, id):
    service = get_object_or_404(Services, id=id)
    if request.method == 'POST':
        service.delete()

        messages.success(request, "Service deleted")
        return redirect('services')
    return render(request, 'delete_service.html', {'service': service})