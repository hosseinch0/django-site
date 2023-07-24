from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from website.models import Contact
from website.forms import NameForm,ContactForm
# Create your views here.

def home_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    return render(request, 'website/contact.html')

def test(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("done")
        
    form = ContactForm()    
    return render(request, "website/test.html", {"form": form})
