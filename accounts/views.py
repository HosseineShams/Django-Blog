from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import LoginForm, ProfileForm, SignupForm
from django.contrib.auth.decorators import login_required
from .models import Profile


def login_view(request):
    template_name = 'accounts/login.html'
    context = {}
    context['form'] = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if not User.objects.filter(username=username).exists():
                messages.warning(request, "User not found!")
                return render(request, template_name, context)

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'You are logged in')
                return redirect('blog:home')
            else:
                messages.error(request, 'Invalid username or password')
                return render(request, template_name, context)
        else:
            messages.error(request, "error!")

    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    messages.success(request, 'You are logged out')
    return redirect('accounts:login')

# @login_required()
# def profile_view(request):
#     template_name = 'accounts/profile.html'
#     context = {}

#     user = request.user

#     initial = {
#         "bio": user.profile.bio
#     }


#     form = ProfileForm(request.POST or None, instance=user, initial=initial)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             bio = form.cleaned_data['bio']
#             user.profile.bio = bio
#             user.profile.save()
#             messages.success(request, 'Your profile has been updated')
#             return redirect('accounts:profile')
#         else:
#             context['form'] = form
#             return render(request, template_name, context)
            
#     context['form'] = form

#     return render(request, template_name, context)  


@login_required()
def profile_view(request):
    template_name = 'accounts/profile.html'
    context = {}

    user = request.user

    try:
        initial = {
            "bio": user.profile.bio
        }
    except Profile.DoesNotExist:
        initial = {}

    form = ProfileForm(request.POST or None, instance=user, initial=initial)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            bio = form.cleaned_data['bio']
            try:
                user.profile.bio = bio
                user.profile.save()
            except Profile.DoesNotExist:
                profile = Profile.objects.create(user=user, bio=bio)
            messages.success(request, 'Your profile has been updated')
            return redirect('accounts:profile')
        else:
            context['form'] = form
            return render(request, template_name, context)
            
    context['form'] = form

    return render(request, template_name, context)  


def signup_view(request):
    template_name = 'accounts/signup.html'
    context = {}
    form = SignupForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your account created successfully')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.refresh_from_db()
            bio = form.cleaned_data['bio']
            # user.profile.bio = bio
            # user.profile.save()
            #-----------------------------------

            try:
                user.profile.bio = bio
                user.profile.save()
            except Profile.DoesNotExist:
                profile = Profile.objects.create(user=user, bio=bio)

            #-----------------------------------
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('blog:home')
        else:
            context['form'] = form
            return render(request, template_name, context)
    else:
        context['form'] = form

    return render(request, template_name, context)