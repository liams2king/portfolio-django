from django.shortcuts import render, redirect
from .models import Project
from .forms import ContactForm

def portfolio(request):
    projects = Project.objects.all()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  # ou vers la même page avec message

    context = {
        'projects': projects,
        'form': form
    }
    return render(request, 'portfolio/index.html', context)


def contact_success(request):
    return render(request, 'portfolio/contact_success.html')
