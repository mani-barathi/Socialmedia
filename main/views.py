from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post

# Create your views here.
# def index(request):
# 	posts = Post.objects.all().order_by('-date_posted')
# 	return render(request,'main/index.html',{'posts':posts})

class PostListView(ListView):
	model = Post
	template_name = 'main/index.html' # by default django sercrches for tamplate with name of <app>/<model>_<viewtype>.html
	context_object_name = 'posts'     # by default it will be objectlist
	ordering = ['-date_posted']
	paginate_by = 5


class PostDetailView(DetailView): 			# uses post_detail.html
	model = Post

class PostCreateView(LoginRequiredMixin,CreateView):   # uses post_form.html
	model = Post
	fields = ['image','caption']
	success_url = reverse_lazy('index') # if the post succesfully posted reverse to index view

	# this method is gonna be called as we create a post, so we are overriding to make sure before it actually validates 
	# we are setting the author = user ,then we are invoking the CreateView form_valid(form)
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):   # uses post_form.html
	model = Post
	fields = ['image','caption']
	success_url = reverse_lazy('index') # if the post succesfully posted reverse to index view

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

		# test_func() is done to check the current loggedin user is same as the post author
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):	# uses post_confirm_delete.html
	model = Post
	success_url = reverse_lazy('index')
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False

# @login_required
# def new_post(request):
# 	return render(request,'main/newpost.html',{})