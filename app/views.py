from django.shortcuts import redirect, render, get_object_or_404
from .models import Intervention, Patient, Procedure
from .forms import PatientForm

def index(request):
    return render(request, "app/index.html")

def patient_list(request):
    patient_list = Patient.objects.all()
    return render(request, "app/patient_list.html", context={"patients": patient_list})


def patient_create(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("app:patient_list")
    else:
        form = PatientForm()

    return render(request, "app/patient_create.html", context={"form": form})