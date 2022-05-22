from django.forms import SlugField
from django.shortcuts import render, redirect
# from django.http import HttpResponse, response
from .models import Meetup, Participant
from .forms import RegistrationForm

# Create your views here.

def index(request):
    # return HttpResponse("This will be displayed on the landing page.")

    # Template's output. The data needs to be injected into the template.
    meetups = Meetup.objects.all()

    # Render will create a HTTP response behind the scene, to return a rendered tempalate.
    # To return a template, that template has to be first defined inside the application's template folder.
    # The path to the template is relative from the template folder.
    # Not just read the HTML content, but will parse, find and execute special instruction and return the final processed content.
    # Third argument (dictionary) : Data which has to be accessible inside the template for output.
    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })

def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                # participant = registration_form.save()

                # Get user email address from the available list, to avoid errors while signing up to
                # multiple meetups with the same email address.
                # cleaned_data holds a dictionary. Key-value pair of all the fields defined.
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)

                selected_meetup.participants.add(participant)
                return redirect('confirm-registration', meetup_slug=meetup_slug)
        
        return render(request, 'meetups/meetup-details.html', {
                'meetup_found': True,
                # 'meetup_title': selected_meetup.title,
                # 'meetup_desc': selected_meetup.description
                'meetup': selected_meetup,
                'form': registration_form
            })

    except Exception as ex:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })

def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html', {
        'organizer_email': meetup.organizer_email
    })