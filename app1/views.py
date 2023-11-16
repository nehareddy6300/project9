from django.shortcuts import render

# Create your views here.


def data_render(request):
    data='nature is beautiful'
    d={'beautiful': data}
    return render(request,'data_render.html',context=d)
