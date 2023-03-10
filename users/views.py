from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import Account
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, IDupdateForm

def update_user_data(user):
    Account.objects.update_or_create(user=user, defaults={'StudentID': user.StudentID},)
 

def register(request):
    if request.method == 'POST':
        
        
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            #newly added
            user.StudentID = form.cleaned_data.get('StudentID')
            update_user_data(user)    

            # load the profile instance created by the signal
            user.save()

            messages.success(request, f'Account created ')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        ID_form = IDupdateForm(request.POST, instance=request.user.account)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid() and ID_form.is_valid():
            u_form.save()
            p_form.save()
            ID_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        ID_form = IDupdateForm()


    context = {
        'u_form' : u_form,
        'p_form' : p_form,
        'ID_form' : ID_form
    }
    return render(request, 'users/profile.html', context)
