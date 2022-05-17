from django.shortcuts import render
# from django.http import HttpResponse, response

# Create your views here.

def index(request):
    # return HttpResponse("This will be displayed on the landing page.")

    # Template's output. The data needs to be injected into the template.
    meetups = [
        {
            'title': 'First meetup',
            'location': 'Basavangudi',
            'genre': 'cultural',
            'slug': 'cult-meetup'
        },
        {
            'title': 'Second meetup',
            'location': 'Jayanagar',
            'genre': 'sports',
            'slug': 'sport-meetup'
        }
    ]

    # Render will create a HTTP response behind the scene, to return a rendered tempalate.
    # The path to the template is relative from the template folder.
    # Not just read the HTML content, but will parse, find and execute special instruction and return the final processed content.
    # Third argument (dictionary) : Data which has to be accessible inside the template for output.
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })