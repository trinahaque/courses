from django.shortcuts import render, redirect, HttpResponse
from .models import Course

def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, "courseapp/index.html", context)

def courses(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')

def destroy(request, id):
    course = Course.objects.get(id=id)
    context = {
        "course": course
    }
    return render(request, "courseapp/destroy.html", context)

def delete(request, id):
    course = Course.objects.get(id=id).delete()
    return redirect('/')

def not_delete(request, id):
    return redirect('/')
