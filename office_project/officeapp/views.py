from django.shortcuts import render, get_object_or_404, redirect
from .models import Office
from .forms import OfficeForm

def office_list(request): 
    offices = Office.objects.all() 
    return render(request, 'officeapp/office_list.html', {'offices': offices})


def office_create(request):
    if request.method == 'POST':
        form = OfficeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('office_list')  
    else:
        form = OfficeForm()
    
    return render(request, 'officeapp/office_form.html', {'form': form}) 


def office_update(request, pk):
    office = get_object_or_404(Office, pk=pk)
    if request.method == 'POST':
        form = OfficeForm(request.POST, instance=office)
        if form.is_valid():
            form.save()
            return redirect('office_list')
    else:
        form = OfficeForm(instance=office)

    return render(request, 'officeapp/office_form.html', {'form': form})
    
def office_delete(request, pk): 
    office = get_object_or_404(Office, pk=pk) 
    if request.method == 'POST': 
        office.delete() 
        return redirect('office_list') 
    return render(request, 'officeapp/office_confirm_delete.html', {'office': office})
