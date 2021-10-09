from django.shortcuts import render,redirect
from .forms import NewDoctorForm, NewPatientForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def signupPatient(request):
    form = NewPatientForm()

    if request.method == "POST":
        form = NewPatientForm(request.POST,request.FILES)
        if form.is_valid():
            password = request.POST["password"]
            confirmation = request.POST["confirm_password"]
            if password != confirmation:
                return render(request, "signup.html", {
                    "message": "Passwords must match."
                })
            form.save(commit=True)
            return redirect('/')
           
        else:
            print('ERROR FORM INVALID')
    
    return render(request,'signuppatient.html',{'form':form})


def signupDoctor(request):
    form = NewDoctorForm()

    if request.method == "POST":
        form = NewDoctorForm(request.POST,request.FILES)
        if form.is_valid():
            password = request.POST["password"]
            confirmation = request.POST["confirm_password"]
            if password != confirmation:
                return render(request, "signup.html", {
                    "message": "Passwords must match."
                })
            form.save(commit=True)
            return index(request)
           
        else:
            print('ERROR FORM INVALID')
    
    return render(request,'signupdoctor.html',{'form':form})