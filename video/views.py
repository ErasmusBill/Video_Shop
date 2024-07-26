from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import *
from django.core.mail import EmailMessage
from django.contrib import messages
from django.db.models import Q
import re

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
      
        if not email or not name or not message or not subject:
            messages.error(request, "All fields are required.")
            return redirect('video:index')

        # Validate email address format
        if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
            messages.error(request, "Invalid email address. Please enter a valid email.")
            return redirect('video:index')
       
        try:
            email_message = EmailMessage(
                subject=f"Message from {name}: {subject}",
                body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email=email,
                to=["erasmuschawey12345@gmail.com"],
            )
            email_message.send()
            messages.success(request, "Email sent successfully!")
            return redirect('video:index')
        
        except Exception as e:
            messages.error(request, f"Error sending email: {e}")
            return redirect('video:index')

    videos = Video.objects.order_by('-date')
    upcoming_videos = Upcoming_video.objects.all()

    return render(request, 'video/index.html', {'videos': videos, 'upcoming_videos': upcoming_videos})

def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        if searched:
            videos = Video.objects.filter(title__icontains=searched)
            if not videos:
                messages.warning(request, "No videos found.")
            return render(request, 'video/searched.html', {'searched': searched, 'videos': videos})
        else:
            messages.warning(request, "Please enter a search term.")
    return render(request, 'video/search.html')

def about(request):
    upcoming_videos = Upcoming_video.objects.all()
    teams = Team.objects.all()
    return render(request, 'video/about.html',{'upcoming_videos':upcoming_videos,'teams':teams})