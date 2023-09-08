from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def home(request):
    # return render(request, 'index.html')
    return redirect("swagger")
