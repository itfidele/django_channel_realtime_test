from django.shortcuts import render

from integers.models import Data

# Create your views here.

def index(request):
    context={
        'text':Data.objects.count()
    }
    return render(request,'index.html',context)