from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import EmployeeForm

@login_required
def home_page_view(request):
    # This handles the Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        employees = Employee.objects.filter(name__icontains=search_query)
    else:
        employees = Employee.objects.all()
        
    return render(request, "home.html", {"employees": employees, "search_query": search_query})

@login_required
def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(request, "add.html", {"form": form})

@login_required
def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, "edit.html", {"form": form})

@login_required
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('home')