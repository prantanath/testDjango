from django.shortcuts import render, redirect
from .forms import add
from .models import Student

def home(request):
    return render(request, "index.html")

def add_std(request):
    if request.method == 'POST':
        form = add(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_std')
        else:
            return render(request, 'index.html', {'form': form})
    return render(request,"index.html")
    

def view_std(request):
    s = Student.objects.all()
    return render(request, 'index.html', {'s': s})

def edit_std(request,id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        form = add(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('view_std')
    else:
        form = add(instance=student)

    return render(request, 'update.html', {'form': form, 'student': student})

def delete(request,id):
    s = Student.objects.get(id=id)
    s.delete()
    return redirect('/')