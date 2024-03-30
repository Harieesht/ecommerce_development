from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
    def __init__(self,*args, **kwargs):
        super(CreateUserForm,self).__init__(*args, **kwargs)
        
        self.fields['email'].required=True
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if User.object.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered")
        if len(email)>=250:
            raise forms.ValidationError("your email is too long.... ")
        
        return email
                
        
            