from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

# Create your views here.
@login_required
def home_page(request):
    post=Post.objects.all()
    return render(request,'home_page.html', {'post':post})
@login_required
def post_detail(request,post_id):
    post=Post.objects.all()
    post_detail=get_object_or_404(Post,id=post_id)
    return render(request,'post_detail.html',{'post_detail':post_detail,'post':post})

def register_view(request):
    if request.method=="POST":
        username=request.POST['username'] 
        password=request.POST['password']

        User.objects.create_user(username=username,password=password)
        return redirect('login_view')
    
    return render(request,'register.html')

def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            return redirect('home_page')
        else:
            return render(request,'login.html',{'error':'invalid login data'})
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')



# def home(request):
#     return render(request,'home.html')

# def p_result(request):
#     if request.method=="POST":
#         name=request.POST.get('name')
#         age=request.POST.get('age')
#         marks=request.POST.get('marks')

#         Students.objects.create(name=name,age=age,marks=marks)

#         return redirect('submit')
    
#     record=Students.objects.all()
#     return render(request,'p_result.html',{'record':record})

# def edit(request,id):
#     record=get_object_or_404(Students,id=id)

#     return render(request,'edit.html',{'record':record})

# def update(request,id):
#     record=get_object_or_404(Students,id=id)

#     if request.method=="POST":
#         record.name=request.POST.get('name')
#         record.age=request.POST.get('age')
#         record.marks=request.POST.get('marks')

#         record.save()
#         return redirect('submit')
    
# def delete(request,id):
#     record=get_object_or_404(Students,id=id)
#     record.delete()

#     return redirect('submit')
