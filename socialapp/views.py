from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,TemplateView,ListView
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from socialapp.models import Posts,Comments,Userprofile
from django.contrib import messages
from socialapp.forms import LoginForm, RegistrationForm ,PostForm,UserdetailForm
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache


# Create your views here.
def signing_required(fn):
    def wrapper(request,*args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"you must login")
            return redirect("signin")
        else:
            return fn(request,args,*kwargs)
    return wrapper
decorators=[signing_required,never_cache]


@method_decorator(decorators,name="dispatch")
class SignUpView(CreateView):
    model=User
    form_class=RegistrationForm
    template_name="register.html"
    success_url=reverse_lazy("signin")

class LoginView(FormView):
    form_class=LoginForm
    template_name="login.html"

    def post(self,request,*args, **kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                return redirect("home")
            else:
                return render(request,self.template_name,{"form":form})



@method_decorator(decorators,name="dispatch")
class IndexView(CreateView,ListView):
    model=Posts
    template_name="index.html"
    form_class=PostForm
    
    success_url=reverse_lazy("home")
    context_object_name="posts"


    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"successfully saved")
        return super().form_valid(form)
    
    # def get_queryset(self):
    #     return Posts.objects.all().exclude(user=self.request.user)

decorators
def add_comment(request,*args, **kwargs):
    post_id=kwargs.get("id")
    pos=Posts.objects.get(id=post_id)
    comm=request.POST.get("comment")
    pos.comments_set.create(comment=comm,user=request.user)
    return redirect("home")

decorators
def like_view(request,*args, **kwargs):
    cmd_id=kwargs.get("id")
    cmd=Posts.objects.get(id=cmd_id)
    cmd.like.add(request.user)
    cmd.save()
    return redirect("home")

class UserprofileView(ListView):
    model=Posts
    template_name: str="userprofile.html"
    context_object_name="posts"

    def get_queryset(self):
        return Posts.objects.filter(user=self.request.user)

decorators
def signout(request,*args, **kwargs):
    logout(request)
    return redirect("signin")










    # def get_context_data(self, **kwargs):
    #     context = super(UserprofileView,self).get_context_data(**kwargs)
    #     context["userd"] = Userprofile.objects.get(user=self.request.user)
    #     return context
    

# class UserdetailView(CreateView):
#     model=Userprofile
#     template_name: str="userprofiledetails.html"
#     form_class=UserdetailForm
#     success_url=reverse_lazy("home")

#     def form_valid(self, form):
#         # form doesnot contain info about user we have to give it seprately
#         form.instance.user=self.request.user 
#         return super().form_valid(form)