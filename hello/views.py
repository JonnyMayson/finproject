
from .models import Task,Task_debate,Task_music,Task_art,Task_vision
from django.views.generic import DetailView, CreateView
from .models import  Category
from django.urls import reverse_lazy

    

class TaskCreate(CreateView):
   
    model= Task
    fields= '__all__'
    success_url = reverse_lazy('tasks')


class TaskCreateMusic(CreateView):
    model= Task_music
    fields= '__all__'
    success_url = reverse_lazy('task-music')
    

class TaskCreateArt(CreateView):
    model= Task_art
    fields= '__all__'
    success_url = reverse_lazy('task-art')    

class TaskCreateVision(CreateView):
    model= Task_vision
    fields= '__all__'
    success_url = reverse_lazy('task-vision')     

class TaskCreateDebate(CreateView):
    model= Task_debate
    fields= '__all__'
    success_url = reverse_lazy('task-debate')       
    

def show_tasks(request):
    tasks = Task_music.objects.all()
    context = {'tasks': tasks}
    return render(request, 'minecraft.html', context)



def index(request):
    return render(request, 'hello/task_list.html', {})


from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages 
from .forms import SignUpForm
from django.views.decorators.csrf import csrf_exempt


def dombyra(request):
    	
    	return render(request, 'clubs/dombyra.html', {})

def music(request):
    	return render(request, 'clubs/music.html', {})

@csrf_exempt
def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			if 'dombyraClub' in username:
				return redirect('add_blog')
			elif 'musicClub' in username:
				return redirect('add_blog')
			elif 'artClub' in username:
				return redirect('add_blog')	
				
			else:
				return redirect('tasks')

		else:
			messages.success(request, ('Сен қателестің'))
			return redirect('login')
	else:
		return render(request, 'registration/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ('You Have Been Logged Out...'))
	return redirect('login')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ('You Have Registered...'))
			return redirect('login')
	else:
		form = SignUpForm()
	
	context = {'form': form}
	return render(request, 'users/signup.html', context)






from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from hello.models import BlogModel
from .forms import BlogForm
from django.urls import reverse_lazy

def details(request, blog_id):
    model = BlogModel.objects.filter(id=blog_id)
    return render(request,'blog_detail.html', {'object_list': model})

class AddBlogView(CreateView):
    model = BlogModel
    form_class = BlogForm
    template_name = 'add_blog.html'
    
class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_categoryView.html'
    fields = '__all__'   

@csrf_exempt
def create_view(request):
    if checkUser(request):
        return redirect('add_category')
    else:
        return redirect('tasks')

def checkUser(request):
    if request.user.is_superuser:
        return True
    else:
        return False

class UpdatePostView(UpdateView): 
    model = BlogModel
    template_name = 'update_blog.html'
    fields = ['title', 'title_tag', 'image', 'content']

class DeleteViewPost(DeleteView): 
    model = BlogModel
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('home')



class HomeView(ListView): 
    model = BlogModel
    template_name = str = 'home.html'
    ordering = ['-id']
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    

def CategoryView(request, cats): 
    category_posts = BlogModel.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})

class ArticleDetailView(DetailView): 
    model = BlogModel
    template_name = str = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context







