from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.contrib import messages, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from .models import List
from .forms import ListForm, FilterForm
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
    usser= auth.get_user(request)
    
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        
        
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = auth.get_user(request).username
            post.save()
            
            if usser.is_staff:
                all_items = List.objects.filter(filter = True) 
            else:
                all_items = List.objects.filter(autor=usser.username,
                                                filter = True)  #filterList(List.objects.all,auth.get_user(request).username)
             
            messages.success(request,('Item has added'))
            return render(request,'home.html',{'all_items':all_items,
                                               'user': auth.get_user(request).username })
            
    
    if usser.is_staff:
        all_items = List.objects.filter(filter = True) 
    else:
        all_items = List.objects.filter(autor=usser.username,
                                        filter = True)  #filterList(List.objects.all,auth.get_user(request).username)
            
    return render(request,'home.html',{'all_items':all_items,
                                           'user': auth.get_user(request).username  })





def filter(request):
   
    if request.method == 'POST':
        form = FilterForm(request.POST or None)
        priort = form['priority'].value()
        isdone = form['do_status'].value()
        
        if "cancel" in request.POST:
            List.objects.all().update(filter = True)
        else:
           
            if isdone == None:   #  all fields without done
                List.objects.filter(priority = priort).update(filter=True)
                List.objects.filter(~Q(priority = priort) ).update(filter=False)
            else:
                List.objects.filter(priority = priort, completed = isdone).update(filter=True)
                List.objects.filter(~Q(priority = priort, completed = isdone) ).update(filter=False)
            
         
        return redirect('home')   
    
        
    else:
        form = FilterForm()
        return  render(request, 'filter.html', {'form': form})
        
    

def filterList(Todolist,username):
    tdlist=[]
    for tv in Todolist:
        if tv.autor ==username :
            tdlist.append(tv)
    
    return tdlist
    



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
    
    
def logOut(request):
    auth.logout(request)
    return redirect('home')
    
    