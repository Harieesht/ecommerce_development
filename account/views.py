from django.shortcuts import render,HttpResponse,redirect
from .forms import CreateUserForm

# Create your views here.
def register(request):
    form=CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('')
        
    context={'form':form}
    return render(request,'account/registration/register.html',context)


def email_verification(request):
    return 

def email_verification_sent(request):
    pass

def email_verification_success(request):
    pass

def email_verification_failed(request):
    pass