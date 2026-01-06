from django.shortcuts import render,redirect
from .models import Employee_Model
# Create your views here.

def Employee_list(request):
    employees = Employee_Model.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def Employee_create(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Designation = request.POST.get('Designation')
        Basic_salary = float(request.POST.get('Basic_salary'))
        HAR_percent = float(request.POST.get('HAR_percent'))
        DA_percent = float(request.POST.get('DA_percent'))
        TA_percent = float(request.POST.get('TA_percent'))
        Bonus = float(request.POST.get('Bonus'))
        Overtime_hours = float(request.POST.get('Overtime_hours'))
        Picture = request.FILES.get('Picture')
        
        
        hra = (HAR_percent / 100) * Basic_salary
        da = (DA_percent / 100) * Basic_salary
        ta = (TA_percent / 100) * Basic_salary
        overtime = Overtime_hours * 100
        overtimes = overtime * 2
        gross_salary = (Basic_salary + hra + da + ta + Bonus + overtimes)
        Employee_Model.objects.create(
            Name = Name,
            Designation = Designation,
            Basic_salary = Basic_salary,
            HAR_percent = hra,
            DA_percent = da,
            TA_percent = ta,
            Bonus = Bonus,
            Overtime_hours = overtimes,
            gross_salary = gross_salary,
            Picture = Picture,
        )
        
        return redirect('employee_list')
    return render(request, 'employee_form.html')


def Employee_update(request, id):
    employee = Employee_Model.objects.get(id=id)

    if request.method == 'POST':
        employee.Name = request.POST['Name']
        employee.Designation = request.POST.get('Designation')
        employee.Basic_salary = request.POST.get('Basic_salary')
        employee.HAR_percent = request.POST.get('HAR_percent')
        employee.DA_percent = request.POST.get('DA_percent')
        employee.TA_percent = request.POST.get('TA_percent')
        employee.Bonus = request.POST.get('Bonus')
        employee.Overtime_hours = request.POST.get('Overtime_hours')
        employee.Picture = request.FILES.get('Picture')
        employee.save()
        return redirect('employee_list')

    return render(request, 'employee_form.html', {'employee': employee})


def Employee_delete(request, id):
    employee = Employee_Model.objects.get(id=id)
    employee.delete()
    return redirect('employee_list')
    