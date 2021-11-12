from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import user_login,question_box,hello

# Create your views here.

def usersignup(request):
	return render(request,'usersignup.html')
	 
def userlogin(request):
		if request.session.get('kuchbhi'):
			return redirect('home')
		else:	
			return render(request,'userlogin.html')
	
def reg(request):
	fn=request.POST['fname']
	email=request.POST['email']
	usr=request.POST['user']
	pwd=request.POST['pass']
	cpwd=request.POST['cpass']
	
	if pwd==cpwd:
		k=user_login.objects.filter(username=usr)
		if len(k)>0:
			return render(request,'usersignup.html',{"msg":"User already Exists"})
		else:	
			a=user_login(fname=fn,email=email,username=usr,password=pwd)
			a.save()
			return redirect('userlogin')
	else:
		return render(request,'usersignup.html',{"msg":"Passwords Do not Match"})
	

	
	
def userlog(request):
	un = request.POST['user']
	pwd = request.POST['pass']
	k=user_login.objects.filter(username=un,password=pwd)
	if len(k)==1:
		request.session['kuchbhi']=un
		return redirect('home')
	else:
		return HttpResponse("Username or Password is Incorrect")
		
def home(request):
	if request.session.get('kuchbhi'):
		return render(request,"home.html")
	else:
		return redirect('userlogin')

def logout(request):
	del request.session['kuchbhi']
	return redirect('userlogin')

def postq(request):
	q=request.POST['question']
	user=request.session.get('kuchbhi')
	k=question_box(question=q,user=user)
	k.save()
	return render(request,"home.html",{"msg":"Question Posted!!"})

def ques(request):
	k=question_box.objects.all()
	return render(request,'ques.html',{"ques":k})
	
def answers(request):
	qid=request.GET['qid']
	k=question_box.objects.filter(id=qid)
	row=k[0]
	a=hello.objects.filter(a=qid)
	return render(request,'answers.html',{"kuchbhi":row,"answers":a})

def addans(request):
	qid = str(request.POST['qid'])
	ans = request.POST['ans']
	user = request.session.get('kuchbhi')
	k=hello(a=qid,b=ans,c=user)
	k.save()
	return redirect('ques')
	