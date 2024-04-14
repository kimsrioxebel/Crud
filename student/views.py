from django.shortcuts import render
from django.shortcuts import render, redirect
from student.forms import StudentsForm
from student.models import Students


# Create your views here.
def index(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = StudentsForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    employees = Students.objects.all()
    return render(request, "show.html", {'employees': employees})


def edit(request, id):
    employee = Students.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    employee = Students.objects.get(id=id)
    form = StudentsForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})


def destroy(request, id):
    employee = Students.objects.get(id=id)
    employee.delete()
    return redirect("/show")
# Create your views here.
