from mysite.form import *
from django.shortcuts import render
from member.models import *
from django.http import HttpResponseRedirect



def loginc(request):
	lerror=[]
	if  not request.session.get('user',False):
		if request.method=="POST":
			l=request.POST
			if ( not l['email'] ) or (not l['password']):
				lerror.append("Fields cannot be left empty")
			if (not '@' in l['email']) or (not '.com' in l['email']):
				lerror.append("Enter a valid email Id")
			if not lerror:

				if user.objects.filter(email=l['email']):
					p=user.objects.get(email=l['email'])
					if l['password']==p.password:
						request.session['user']=p.first_name
						return HttpResponseRedirect("/upload/")
					else:
						lerror.append("Incorrect Password")
				else:
					lerror.append("Sorry the account doesnt exist")
		return render(request,"login.html",{'form':login(),'lerror':lerror})
	else:
		return HttpResponseRedirect("/upload/")




def signupc(request):
	serror=[]

	if request.method=="POST":
		l=request.POST
		if (not l['cf_password']) or (not l['semail']) or (not l['first_name']) or (not l['last_name']) or (not l['spassword']) or (not l['dob']):
			serror.append("Fields Cannot be left blank")
		if (not '@' in l['semail']) or (not '.com' in l['semail']):
			serror.append("Enter a valid email Id")
		if not l['spassword']==l['cf_password']:
			serror.append("Sorry the passwords do not match")
		if not serror:
			user.objects.create(email=l['semail'],first_name=l['first_name'],last_name=l['last_name'],password=l['spassword'],dob=l['dob'])
			return render(request,"lsignup.html",)

	return render(request,"signup.html",{'sform':signup(),'serror':serror})

def add(request):
	if  request.session.get('user',False):
		if request.method == 'POST':
			form = fuf(request.POST, request.FILES)
			if form.is_valid():
				request.POST['name']=request.session['user']
				instance = fu(name=request.POST['name'],ufile=request.FILES['ufile'])
				instance.save()
				return HttpResponseRedirect("/upload")
			else:
				form = fuf()
		else:
			form=fuf()
		name=request.session['user']
		return render(request, 'home.html', {'fuf': fuf,'name':name})
	else:
		return HttpResponseRedirect("/")
def logout(request):

	del request.session['user']
	return HttpResponseRedirect("/")
def upload(request):
	if  request.session.get('user',False):
		name=request.session['user']
		imodel=fu.objects.all()[::-1]
		return render(request, 'home1.html', {'imodel':imodel,'name':name})
	else:
		return HttpResponseRedirect("/")
