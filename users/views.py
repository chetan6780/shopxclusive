import imp
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        print(request.POST)
        form = NewUserForm(request.POST)
        if form.is_valid():
            print("true hua")
            user = form.save()
            return redirect('/shop/products')

    form = NewUserForm()
    context = {
        'form': form,
    }

    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    return render(request, 'users/profile.html')
