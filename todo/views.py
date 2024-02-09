from django.shortcuts import render,redirect

from django.views.generic import View

from todo.models import Task

from django import forms

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

class TaskForm(forms.ModelForm):

    class Meta:
        model=Task
        exclude=("created_date",)


class RegistrationForm(forms.ModelForm):

    class Meta:
        model=User
        fields=["username","email","password"]

class LoginForm(forms.Form):

    username=forms.CharField()
    password=forms.CharField()


class TaskListView(View):
    def get(self,request,*args,**kwargs):
        qs=Task.objects.all()
        return render(request,"task_list.html",{"data":qs})
    

class TaskCreateView(View):
    def get(self,request,*args,**kwargs):
        form=TaskForm()
        return render(request,"task_add.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task-list")
        else:
            return render(request,"task_add.html",{"form":form})
        
class TaskDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        return render(request,"task_detail.html",{"data":qs})
    
class TaskDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Task.objects.get(id=id).delete()
        return redirect("task-list")
    
class TaskUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        task_object=Task.objects.get(id=id)
        form=TaskForm(instance=task_object)  
        return render(request,"task_update.html",{"form":form})    

    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        task_object=Task.objects.get(id=id)
        form=TaskForm(request.POST,instance=task_object)
        if form.is_valid():
            form.save()
            return redirect("task-list")
        else:
            return render(request,"task_update.html",{"form":form})   


class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            # form.save()
            User.objects.create_user(**form.cleaned_data)
            return redirect("signin")
        else:
            return render(request,"register.html",{"form":form})
        
class SigninView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"signin.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            u_name=data.get("username")
            pwd=data.get("password")
            user_obj=authenticate(request,username=u_name,password=pwd)
            if user_obj:
                login(request,user_obj)
                return redirect("task-list")
        return render(request,"signin.html",{"form":form})
    
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")



  
     
 
