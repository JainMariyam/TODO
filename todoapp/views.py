from django.shortcuts import render,redirect
from django.views.generic import View
from todoapp.forms import UserForm,LoginForm,TodoForm
from django.contrib.auth import authenticate,login,logout
from todoapp.models import Todos
from django.utils.decorators import method_decorator # function based decoratorine class based ie..,method baswd decorator aakan
# Create your views here.

def siginin_required(fn):# decorator nov 29 ,here we use two decorators 1)for login cheythittundonnu ariyan,2)owner thanne aano login cheytha user nnu ariyan
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            return fn(request,*args,**kwargs)
    return wrapper

def ownerpermission_required(fn):
    def wrapper(request,*args,**kwargs):
        id=kwargs.get('pk')#urlil ninnu id edukan
        todo_object=Todos.objects.get(id=id) # aa id ulla todo object edukan
        if todo_object.user!=request.user: #ownerum userum same aano nnu nokkan
            logout(request)
            return redirect('login')
        else:
            return fn(request,*args,**kwargs)
    return wrapper


decs=[siginin_required,ownerpermission_required]
class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=UserForm()
        return render(request,"register.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            print("account created")
            return redirect('register')
        else:
            return render(request,"register.html",{"form":form})

class LoginView(View):#nov 23
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{'form':form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get('username')# usercreation form use cheyunnathukondu form.save,encryption ellam athil thanne und
            pwd=form.cleaned_data.get('password')
            user_object=authenticate(request,username=uname,password=pwd)

            if user_object:
                login(request,user_object)
                print('valid')
                return redirect('index')
        print('invalid')
        return render(request,"login.html",{'form':form})
    
@method_decorator(siginin_required,name="dispatch")#ivide list,add maathre cheyunnullu,so ownerpermission required venda
class IndexView(View):
    def get(self,request,*args,**kwargs):
        qs=Todos.objects.filter(user=request.user)# nov 23
        form=TodoForm()
        pending_count=Todos.objects.filter(status='todo',user=request.user).count()# nov 28 to count the no:
        progress_count=Todos.objects.filter(status='inprogress',user=request.user).count()# login cheytha userinte todos kaanikan user=request.user
        finished_count=Todos.objects.filter(status="completed",user=request.user).count()
        
        return render(request,'index.html',{'form':form,
                                            'data':qs,
                                            'pending':pending_count,
                                            'progress':progress_count,
                                            'finished':finished_count})
    def post(self,request,*args,**kwargs):
        form=TodoForm(request.POST)
        if form.is_valid():
            form.instance.user=request.user # nov 23 form.instance means form=Todoform koduthittund athinte user fieldileku value edukan ie.,ippo request.postil name maathre ullu namuku user venam,status default todo kodthittund
            form.save()
            return redirect('index')
        else:
            return render(request,"index.html",{'form':form})
        

#todos/{id}/?status=inprogress
@method_decorator(decs,name='dispatch')# delete,update actual owner aanenkil mathre perform cheyuu
class TodoUpdateView(View):# nov 28
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')# url il koduthekunna id ulla objectine edukan
        if 'status'in request.GET:#url il status undenkil
            value=request.GET.get("status")
            if value=='inprogress':# mobileil brand=samsung same logic ie., urlil status=inprogress means inprogressnnu aakanamenkil
                Todos.objects.filter(id=id).update(status='inprogress')
            elif value=='completed':
                Todos.objects.filter(id=id).update(status='completed')
        return redirect('index')


@method_decorator(decs,name='dispatch')   
class TodoDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Todos.objects.filter(id=id).delete()
        return redirect('index')
    
@method_decorator(siginin_required,name='dispatch')
class LogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('login')


    
