from django.shortcuts import render

# Create your views here.
def ifelifcondition(request):
    d={'a':100,'b':200,'c':300}
    return render(request,'ifelifcondition.html',d)