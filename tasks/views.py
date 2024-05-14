from django.views import View
from django.shortcuts import render, redirect
from . models import Task
from .forms import taskcreateform
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin





class detailtask(LoginRequiredMixin,View):
    def get(self, request,task_id):
        task=Task.objects.get(id=task_id)
        return render(request,'tasks/detail.html',{'task':task})
        
    def post(self, request):
        pass

class deletetask(LoginRequiredMixin,View):
    def get(self, request, task_id):
        task=Task.objects.get(id=task_id)
        task.delete()
        return redirect('accounts:home_user',request.user.id)


class ceratetask(LoginRequiredMixin,View):
    form_class=taskcreateform
    def get(self, request):
        return render(request,'tasks/create.html',{'form':self.form_class})
    


    def post(self, request):
        form=self.form_class(request.POST)
        if form.is_valid():
            new_task=Task.objects.create(
                user=request.user,
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                complite=form.cleaned_data['complite']
            )
            # new_task.save(commit=False)
            # new_task.user=request.user
            new_task.save()
            messages.success(request,'new task added','success')
            # return redirect('accounts:home')
            return redirect('accounts:home_user',request.user.id)
        messages.error(request,'faild!!','danger')
        return  render(request, 'tasks/create.html',{'form':form})
    

class updatetask(LoginRequiredMixin,View):
    def get(self, request, task_id):
         task=Task.objects.get(pk=task_id)
         form=taskcreateform(instance=task)
         return render(request,'tasks/update.html',{'form':form})




       
    def post(self, request, task_id):
        task=Task.objects.get(pk=task_id)
        form=taskcreateform(request.POST,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,'updated successfully','success')
            return  redirect('accounts:home_user', request.user.id)
       
        messages.error(request,'faild!!','danger')
        return render(request,'tasks/update.html',{'form':form})
