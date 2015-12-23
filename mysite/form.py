from django import forms
class login(forms.Form):
	email=forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder':'Email'}))
	password=forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder':'Password'}))



class signup(forms.Form):
	semail=forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder':'Email'}))
	first_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'First name'}))
	last_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
	spassword=forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
	cf_password=forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
	dob=forms.DateField(widget=forms.TextInput(attrs={'placeholder':'Date of birth YYYY-MM-DD'}))

class fuf(forms.Form):
    name=forms.CharField(required=False)
    ufile=forms.FileField(required=True)
