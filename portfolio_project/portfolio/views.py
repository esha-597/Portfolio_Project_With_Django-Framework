from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile, Skill, Experience, Education, Project, Contact

DEFAULT_USERNAME = 'esha'  # Replace with your actual default username


def home(request, username=None):
    if username:
        user = get_object_or_404(User, username=username)
    else:
        user = get_object_or_404(User, username=DEFAULT_USERNAME)

    profile = Profile.objects.filter(user=user).first()  # Fetching the header for the user
    skills = Skill.objects.filter(user=user)
    experience = Experience.objects.filter(user=user)
    education = Education.objects.filter(user=user)
    projects = Project.objects.filter(user=user)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        contact = Contact(user=user, name=name, email=email, message=message)
        contact.save()

        messages.success(request, 'Your message has been submitted successfully!')

        request.session['form_submitted'] = True

        if username:
            return redirect('user_home', username=username)
        else:
            return redirect('home')

        # Clear the form submission flag after redirecting
    form_submitted = request.session.pop('form_submitted', False)

    context = {
        'profile': profile,
        'skills': skills,
        'experience': experience,
        'education': education,
        'projects': projects,
        'portfolio_user': user,
    }

    return render(request, 'portfolio/home.html', context)