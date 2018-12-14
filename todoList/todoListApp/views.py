from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import List
from .forms import ListForm
from django.contrib.auth import login
# Create your views here.

# This function is invoked to return html template page to client when the request url is http://localhost:8000/hello_world/hello
def hello_world(request):
    # The html file path relative to TEMPLATE DIRS directory defined in DjangoProjectExample / settings.py file..
    hello_world_file_path = 'E:\\Jack\\Documents\\eclipse\\todoList\\todoListApp\\pages\\index.html'  #'todoListApp\\pages\\index.html'
    # The context object will send back to client, it is a dictionary object contains a Message.
    context = {'Message' : 'Welcome to Django world.'}
    return  HttpResponse("<h3> hello </h3>") #render(request, hello_world_file_path, context)

def home(request):
    #return render(request,"home.html",{})
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request,('Item has added'))
            return render(request,'home.html',{'all_items':all_items})
            
    else:
        all_items = List.objects.all
        return render(request,'home.html',{'all_items':all_items})
    

def delete(request,list_id):
    item = List.objects.get( pk = list_id)
    item.delete()
    messages.success(request, ('Item deleted!'))
    return redirect('home')


def cross_off(request,list_id):
    item = List.objects.get( pk = list_id)
    item.completed = True
    item.save()

    return redirect('home')


def uncross(request,list_id):
    item = List.objects.get( pk = list_id)
    item.completed = False
    item.save()

    return redirect('home')


# Class form registration
class RegisterFormView(FormView):
    form_class = UserCreationForm
    
    #link to good registration
    succes_url = "/home/"
    
    #template to view
    template_name = "register.html"
    
    def form_valid(self, form):
        #create user if data valid
        form.save()
        
        return super(RegisterFormView,self).form_valid(self, form)
    
 # CLass form authendification
class LoginFormView(FormView):
    form_class = AuthenticationForm
    
    #login template
    template_name = "login.html"
    
    #if good go home
    success_url = "/"
    
    def form_valid(self,form):
        self.user = form.get_user()
    
        #do auth
        login(self.request,self.user)
        return super(LoginFormView, self).form_valid(form)
    
    

    