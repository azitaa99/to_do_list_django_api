from django.shortcuts import render,redirect
from django.views import View
from accounts.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from tasks.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin



class Homeview(View):
    def get(self,request,user_id=None):
        
        if user_id:
            user=User.objects.get(pk=user_id)
            to_do=Task.objects.filter(user=user)
            incom_task=to_do.filter(complite=False).count()
            val=''
            if request.GET.get('filterby'):
                to_do= to_do.filter(title__contains=request.GET['filterby'])
                val=request.GET['filterby']
                
            return render(request,'accounts/index.html',{'doing':to_do,'incom_tasks':incom_task,'val':val})

        return render(request, 'accounts/index.html')


class UserRegister(View):
    def get(self,request):
        form_class= RegisterForm()
        return render(request, 'accounts/register.html',{'form':form_class})
    
    def post(self, request):
        form=RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username= form.cleaned_data['username'],
                                     email=form.cleaned_data['email'],
                                      password= form.cleaned_data['password'])
            messages.success(request,'you register successfully','success')
            return redirect('accounts:home')
        messages.error(request,'register faild!','danger')
        return render(request,'accounts/register.html',{'form':form})


class LoginView(View):
    from_class=LoginForm
    def get(self, request):
        return render(request,'accounts/login.html',{'form':self.from_class})
        
    

    def post(self, request):
        
        form= self.from_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            
            user=authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'you login sucessfully','success')
                return redirect('accounts:home_user',user.id)
            messages.error(request,'this user is not register','danger')
            return redirect('accounts:login')
        messages.error(request,'not correct','danger')
        return redirect('accounts:login')



class logoutView(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.success(request,'you logout sucessfully','success')
        return redirect('accounts:home')