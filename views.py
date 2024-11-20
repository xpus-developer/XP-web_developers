from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def portfolio(request):
    return render(request, 'portfolio.html')



from django.shortcuts import render, redirect
from .forms import ContactMessageForm

def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('thank_you')  # Redirect to a thank you page after successful submission
    else:
        form = ContactMessageForm()

    return render(request, 'contact.html', {'form': form})


def do(request):
    return render(request, 'do.html')

from django.shortcuts import render

def thank_you(request):
    return render(request, 'thank_you.html')

