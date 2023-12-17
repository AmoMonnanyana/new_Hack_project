from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.models import Group


# Create your views here.

# User registration and login

def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            role = form.cleaned_data['role']
            
            if role == 'customer':
                group_name = 'customer'  
            elif role == 'staff':
                group_name = 'staff'
            elif role =='supplier':
                group_name = 'supplier'
            elif role == 'accountant':
                group_name = 'accountant'
            
            group = Group.objects.get(name=group_name)
            user.groups.add(group)

            return redirect('user-login')

    else:
        form = CreateUserForm()

    context =  {
            'form': form,
        }    
    return render(request, 'register.html', context)
