from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app1_string(request):
    return HttpResponse('first app1_string response')


def app1_html(request):
    return render(request,'app1_html.html')