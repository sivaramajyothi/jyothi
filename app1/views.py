from django.shortcuts import render

# Create your views here.
def a1_first(request):
    d={'a':5489}
    return render(request,'a1_first.html',d) 

    def a1_first(request):
        d={'a':6769}
        return render(request,'a1_first.html',d)
