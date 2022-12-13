from django import forms  
from .models import Employee , Login
Shifts=[
    ('I','First'),
    ('II','Second'),
]
class EmployeeForm(forms.ModelForm):  
    Code=forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter employee code'}))
    Name=forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter employee name'}))
    Email=forms.EmailField(widget= forms.TextInput(attrs={'placeholder':'Enter employee email'}))
    #Shift=forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter employee shift'}))
    Dept=forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter employee dept'}))
    Shift=forms.CharField(widget=forms.Select(choices=Shifts))
    class Meta:  
        model = Employee  
        fields = "__all__"  
class LoginForm(forms.ModelForm):
    Username = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter username'}))
    Password =  forms.CharField(max_length=32,widget=forms.PasswordInput)
    class Meta:
        model = Login
        fields = "__all__" 
class SignUpForm(forms.ModelForm):
    Firstname = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter first name'}))
    Lastname =  forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter last name'}))
    Username = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter username'}))
    Password =  forms.CharField(max_length=32,widget=forms.PasswordInput)
    Email=forms.EmailField(widget= forms.TextInput(attrs={'placeholder':'Enter employee email'}))
    Dob=forms.DateField(widget= forms.TextInput(attrs={'placeholder':' Enter employee dob'}))
    class Meta:
        model = Login
        fields = "__all__" 