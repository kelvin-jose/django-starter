from django.shortcuts import render
from signup.models import UserModel

# Create your views here.

def index(request):
    return render(request,'signup/index.html')

def save(request):
    if request.method == 'POST':
        userModel = UserModel()
        userModel.first_name = request.POST.get('first_name')
        userModel.last_name = request.POST.get('last_name')
        userModel.regno = request.POST.get('regno')
        userModel.email = request.POST.get('email')
        userModel.phone = request.POST.get('phone')
        userModel.course = request.POST.get('course')
        userModel.save()
    return render(request,'signup/index.html')

def show(request):
    data = UserModel.objects.all()
    return render(request,'signup/show.html',{
    'data': data
})
