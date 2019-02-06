from django.shortcuts import render
from ProjectApp.models import Users
# Create your views here.

def index(request):
    return render(request,'ProjectApp/index.html')

def users(request):

    user_list = Users.objects.order_by('firstname')
    user_dict = {'users':user_list}
    return render(request,'ProjectApp/users.html',context=user_dict)
