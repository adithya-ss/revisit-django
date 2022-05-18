from django.forms import SlugField
from django.shortcuts import render
# from django.http import HttpResponse, response
from .models import Meetup

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
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': True,
            'meetup_title': selected_meetup.title,
            'meetup_desc': selected_meetup.description
        })
    except Exception as ex:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })