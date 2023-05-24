from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2_string(request):
    return HttpResponse('<h1>this is app2_string as response</h1>')


def app2_html(request):
    return render(request,'app2_html.html')