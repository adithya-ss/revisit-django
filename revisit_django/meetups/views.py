from django.shortcuts import render
# from django.http import HttpResponse, response

# Create your views here.

def index(request):
    # return HttpResponse("This will be displayed on the landing page.")

    # Render will create a HTTP response behind the scene, to return a rendered tempalate.
    # The path to the template is relative from the template folder.
    # Not just read the HTML content, but will parse, find and execute special instruction and return the final processed content.
    return render(request, 'meetups/index.html')