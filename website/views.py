from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm,ContactForm,NewsLetterForm
from django.contrib import messages
# Create your views here.

def home_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS, "Your information has been received successfully")
        else:
            messages.add_message(request, messages.SUCCESS,"ERROR: Something went wrong")
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


def test(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("done")
        
    form = ContactForm()    
    return render(request, "website/test.html", {"form": form})


def newsletter_view(request):
    if request.method == "POST":
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')