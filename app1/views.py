from django.shortcuts import render



def home(request):
    factorial=1
    
    n1=5
    for i in range(1,n1+1,1):
        factorial=factorial*i
       
    n2=5
    squre1=n2*n2
    return render(request,'app1\index.html',{'param1':factorial,'param2':n1,'param4':squre1,'param3':n2})


    