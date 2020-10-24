from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserSignUpForm,UserUpdateForm,ProfileUpdateForm
# from .models import Profile

# Create your views here.
# def index(request):
# 	return render(request,'users/index.html',{})

def signup(request):
	if request.method == 'POST':
		form = UserSignUpForm(request.POST)	
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			form.save()
			subject = 'Welocome to Social Media'
			msg = f'Hi {username}, We are glad to have you here!. Start sharing you Posts.'
			sender = 'youremail.s@gmail.com'
			receiver = [email,]
			send_mail(subject,msg, sender, receiver)
			messages.success(request,f'Account created for {username}!')
			return redirect('login')			
	else:	
		form = UserSignUpForm()
	return render(request,'users/signup.html',{'form':form})

@login_required
def profile(request):			# edit my profile view
	if request.method=='POST':
		u_form = UserUpdateForm(request.POST,instance=request.user)
		p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		# instance is passsed to form because it has to know what User and Profile it has to update
		# if it is not passed it will try to create an another new object for User and Profile
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Profile Successfully Updated')
			return redirect('profile')		

	#  Passing the user, profile objects to the forms makes sures to populate pre existing data to it
	u_form = UserUpdateForm(instance=request.user)			
	p_form = ProfileUpdateForm(instance=request.user.profile)	
	return render(request,'users/profile.html',{'u_form':u_form,'p_form':p_form})

@login_required
def any_profile(request,user):
	user = User.objects.filter(username=user).first()
	posts = user.post_set.all().order_by('-date_posted')
	if user is not None:
		context={
			'userobj': user,
			'posts'  : posts 
		}
		return render(request,'users/any_profile.html',context)	
	else:
		return render(request,'users/page_not_found.html',{})
@login_required
def search_user(request):
	if request.method=='GET':
		search_user = request.GET.get('q')
	# kwargs = { '{0}__{1}'.format('first_name','icontains'):search_user}
	result = User.objects.filter(Q(first_name__icontains=search_user) | 
								 Q(last_name__icontains=search_user) |
								 Q(username__icontains=search_user) )
	context={ 'users':result ,'fetch':True,'search_user':search_user}
	if len(result)==0:
		context['fetch'] = False
	return render(request,'users/search_user.html',context)

@login_required
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user,request.POST)
		if form.is_valid():
			user = form.save()

			update_session_auth_hash(request,user)		# takes the updated user and request
			#This function takes the current request and the updated user object from which the new session hash will be derived and 
			#updates the session hash appropriately. It also rotates the session key so that a stolen session cookie will be invalidated.
			
			messages.success(request,'Your Password is Successfully Updated!')
			return redirect('index')			
	form = PasswordChangeForm(request.user)
	return render(request,'users/change_password.html',{'form':form})

@login_required
def settings(request):
	return render(request,'users/settings.html')


def about(request):
	return render(request,'users/about.html',{})