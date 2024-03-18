from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login , logout,authenticate
from .forms import CreateUserForm
#python manage.py runserver 0.0.0.0:8000
def login_view(request):
    if request.method == 'POST':
        # Extract username and number from POST data
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        # Query the database to find a user with the provided username
        user = authenticate(request,username=username,password=password)
        
        
        
        if user is not None:  # Check if user exists
            # Check if the provided number matches the number stored in the database
            
            print('hi')
            
            # If number matches, log the user in and redirect to the index page
            login(request,user)
            return redirect('index')
            
        else:
            # If the user doesn't exist, render login page with an error message
            return render(request, 'login.html', {'error': 'Invalid username'})
    else:
        # If the request method is not POST, render the login page
        return render(request, 'login.html')
def signup(request):
    
    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login_view")


        context = {'registerform':form}

        return render(request, 'regester.html', context=context)
    else:
        context = {'registerform':form}
        return render(request, 'regester.html' , context=context)
@login_required
def index(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login_view')
    else:
        active = {'Home': "active", 'About': "", 'Service': "", 'Project': "", 'Pages': "", 'OurTeam': "", 'Testimonial': "", 'P404': ""}
        
        return render(request, 'index.html', {'active': active })

@login_required
def about(request):
    active = {'Home': "", 'About': "active", 'Service': "", 'Project': "", 'Pages': "", 'OurTeam': "", 'Testimonial': "", 'P404': ""}
    return render(request, 'about.html', {'active': active })

@login_required
def contact(request):
    active = {'Home': "", 'About': "", 'Service': "", 'Project': "", 'Pages': "", 'OurTeam': "", 'Testimonial': "", 'P404': "", 'Contact': "active"}
    return render(request, 'contact.html', {'active': active })

@login_required
def service_view(request):
    active = {'Home': "", 'About': "", 'Service': "active", 'Project': "", 'Pages': "", 'OurTeam': "", 'Testimonial': "", 'P404': ""}
    return render(request, 'service.html', {'active': active })

@login_required
def project_view(request):
    active = {'Home': "", 'About': "", 'Service': "", 'Project': "active", 'Pages': "", 'OurTeam': "", 'Testimonial': "", 'P404': ""}
    return render(request, 'project.html', {'active': active })

@login_required
def team_view(request):
    active = {'Home': "", 'About': "", 'Service': "", 'Project': "", 'Pages': "", 'OurTeam': "active", 'Testimonial': "", 'P404': ""}
    return render(request, 'team.html', {'active': active })

@login_required
def testimonial_view(request):
    active = {'Home': "", 'About': "", 'Service': "", 'Project': "", 'Pages': "", 'OurTeam': "", 'Testimonial': "active", 'P404': ""}
    return render(request, 'testimonial.html', {'active': active })

@login_required
def page_not_found_view(request):
    active = {'Home': "", 'About': "", 'Service': "", 'Project': "", 'Pages': "", 'OurTeam': "", 'Testimonial': "", 'P404': "active"}
    return render(request, '404.html', {'active': active })
