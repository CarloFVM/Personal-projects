from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<em>My Second Project</em>")

def help(request):
    my_dict={'insert_me':"This page is going to have contacts to get help"}
    return render(request,'protwo/help.html',context=my_dict)
