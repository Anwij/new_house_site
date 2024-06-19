from django.shortcuts import render, redirect, get_object_or_404
from .models import Application
from .forms import ApplicationForm
from django.contrib import messages
# Create your views here.


def add_application(request):
    if request.method == 'POST':
        application_form = ApplicationForm(request.POST)
        if application_form.is_valid():
            application_form.save()
            messages.success(request, "Заявка принята.")
            return redirect('application:add_application')
    else:
        application_form = ApplicationForm()
    return render(request, 'application/add_application.html', {'application_form': application_form})


def all_application(request):
    application_list = Application.objects.order_by('-created_at')
    return render(request, 'application/all_application.html', {'application_list': application_list})


def application_detail(request, pk):
    application = get_object_or_404(Application, pk=pk)
    return render(request, 'application/application_detail.html', {'application': application})


def delete_application(request, pk):
    application = get_object_or_404(Application, pk=pk)
    application.delete()
    return redirect('application:all_application')