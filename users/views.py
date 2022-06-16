from django.shortcuts import redirect, render
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User


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


def create_profile(request):
    if request.method == 'POST':
        contact_number = request.POST.get('contact_number')
        image = request.FILES['upload']
        user = request.user
        profile = Profile(contact_number=contact_number,
                          image=image, user=user)
        profile.save()
    return render(request, 'users/create_profile.html')


def seller_profile(request, id):
    seller = User.objects.get(id=id)
    context = {
        'seller': seller
    }
    return render(request, 'users/seller_profile.html', context)
