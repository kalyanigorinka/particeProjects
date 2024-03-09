from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def demo(request):
    # return HttpResponse("my first project")
    c = " "
    if request.method=="POST":
        n1=eval(request.POST.get("a"))
        n2=eval(request.POST.get("b"))
        opr=request.POST.get("opr")

        if opr=="+":
           c=n1+n2
      
        elif opr=="-":
           c=n1-n2

        elif opr=="*":
           c=n1*n2

        elif opr=="/":
           c=n1/n2

        elif opr=="**":
           c=n1**n2

    return render (request,'cal.html',{"o":c})