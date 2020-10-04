from django.shortcuts import render
from app.models import files
from app.models import user
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from django.shortcuts import render, redirect


# Create your views here.
def search(request):
    if request.method == 'GET':
        return render(request,'search.html')
    elif request.method == 'POST':
        input = request.POST['q']
        ss = user.objects.filter(user_name__contains=input)
        v =''
        for v in ss:
            v = v.id
        app_file = files.objects.filter(id__iexact=v)
        return render(request,'search.html',{'show':app_file, 'userdata' :ss})

